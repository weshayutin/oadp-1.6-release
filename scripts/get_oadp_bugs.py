#!/usr/bin/env python3
"""
Query OADP Jira issues (Bugs, Tasks, Epics, Stories) for a given fixVersion and
generate a markdown report grouped by issue type, then by assignee.

Auth: set JIRA_EMAIL and JIRA_API_TOKEN env vars, or create a ~/.netrc entry
for redhat.atlassian.net.

Usage:
    python3 get_oadp_bugs.py                          # defaults to OADP 1.6.0
    python3 get_oadp_bugs.py --version "OADP 1.5.0"
    python3 get_oadp_bugs.py -o oadp-1.6.0-bugs.md   # write to file
    python3 get_oadp_bugs.py --qe                     # QE report: ON_QA/VERIFIED grouped by QA Contact
"""

import argparse
import base64
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(REPO_ROOT, "output")

JIRA_SITE = "redhat.atlassian.net"
API_BASE = f"https://{JIRA_SITE}/rest/api/3"
DEFAULT_VERSION = "OADP 1.6.0"
EXCLUDED_STATUSES = ("MODIFIED", "Closed", "ON_QA", "Dev Complete", "Verified")
QE_STATUSES = ("ON_QA",)
QA_CONTACT_FIELD = "customfield_10470"
PAGE_SIZE = 100

PRIORITY_ORDER = {
    "Blocker": 0, "Critical": 1, "Major": 2, "Normal": 3,
    "Minor": 4, "Trivial": 5, "Undefined": 6,
}


def get_auth_header():
    email = os.environ.get("JIRA_EMAIL", "")
    token = os.environ.get("JIRA_API_TOKEN", "")
    if email and token:
        creds = base64.b64encode(f"{email}:{token}".encode()).decode()
        return f"Basic {creds}"

    try:
        import netrc
        auth = netrc.netrc().authenticators(JIRA_SITE)
        if auth:
            creds = base64.b64encode(f"{auth[0]}:{auth[2]}".encode()).decode()
            return f"Basic {creds}"
    except Exception:
        pass

    print(
        "ERROR: Set JIRA_EMAIL + JIRA_API_TOKEN env vars, or add a ~/.netrc entry for "
        f"{JIRA_SITE}",
        file=sys.stderr,
    )
    sys.exit(1)


def jira_search(jql, auth_header, extra_fields=None):
    """Return all matching issues, handling pagination via nextPageToken."""
    issues = []
    fields = "summary,status,priority,created,labels,assignee,issuetype"
    if extra_fields:
        fields += "," + ",".join(extra_fields)
    next_token = None
    while True:
        params = {"jql": jql, "maxResults": PAGE_SIZE, "fields": fields}
        if next_token:
            params["nextPageToken"] = next_token
        qs = urllib.parse.urlencode(params)
        req = urllib.request.Request(
            f"{API_BASE}/search/jql?{qs}",
            headers={
                "Authorization": auth_header,
                "Accept": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        issues.extend(data["issues"])
        if data.get("isLast", True):
            break
        next_token = data.get("nextPageToken")
        if not next_token:
            break
    return issues, len(issues)


def fetch_child_issues(parent_keys, auth_header):
    """Fetch subtasks/child issues for a list of parent issue keys.

    Returns a dict mapping parent key -> list of child issue dicts.
    """
    if not parent_keys:
        return {}
    keys_str = ", ".join(parent_keys)
    jql = f"parent in ({keys_str}) ORDER BY created ASC"
    issues = []
    fields = "summary,status,assignee,issuetype,parent"
    next_token = None
    while True:
        params = {"jql": jql, "maxResults": PAGE_SIZE, "fields": fields}
        if next_token:
            params["nextPageToken"] = next_token
        qs = urllib.parse.urlencode(params)
        req = urllib.request.Request(
            f"{API_BASE}/search/jql?{qs}",
            headers={
                "Authorization": auth_header,
                "Accept": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        issues.extend(data["issues"])
        if data.get("isLast", True):
            break
        next_token = data.get("nextPageToken")
        if not next_token:
            break

    by_parent = defaultdict(list)
    for issue in issues:
        parent_key = (issue["fields"].get("parent") or {}).get("key")
        if parent_key:
            by_parent[parent_key].append(issue)
    return dict(by_parent)


ISSUE_TYPES = ("Bug", "Task", "Epic", "Story")
STORY_STATUSES = ("New", "To Do", "In Progress")
ISSUE_TYPE_ORDER = {t: i for i, t in enumerate(ISSUE_TYPES)}


def build_jql(version, excluded_statuses, issue_types=ISSUE_TYPES):
    statuses = ", ".join(f'"{s}"' for s in excluded_statuses)
    non_story_types = ", ".join(t for t in issue_types if t != "Story")
    story_statuses = ", ".join(f'"{s}"' for s in STORY_STATUSES)
    parts = []
    if non_story_types:
        parts.append(
            f'(project = OADP AND fixVersion = "{version}" '
            f"AND issuetype in ({non_story_types}) "
            f"AND status not in ({statuses}))"
        )
    if "Story" in issue_types:
        parts.append(
            f'(project = OADP AND fixVersion = "{version}" '
            f"AND issuetype = Story "
            f"AND status in ({story_statuses}))"
        )
    return " OR ".join(parts) + " ORDER BY priority DESC, created DESC"


def build_qe_jql(version, statuses=QE_STATUSES, issue_types=ISSUE_TYPES):
    status_list = ", ".join(f'"{s}"' for s in statuses)
    types = ", ".join(issue_types)
    return (
        f'project = OADP AND fixVersion = "{version}" AND issuetype in ({types}) '
        f"AND status in ({status_list}) "
        f"ORDER BY priority DESC, created DESC"
    )


def format_issue_row(issue):
    f = issue["fields"]
    key = issue["key"]
    summary = f["summary"]
    priority = f.get("priority", {}).get("name", "Undefined")
    status = f.get("status", {}).get("name", "")
    created = f["created"][:10]
    labels = ", ".join(f.get("labels", []))
    link = f"https://{JIRA_SITE}/browse/{key}"
    return f"| [{key}]({link}) | {summary} | {priority} | {status} | {created} | {labels} |"


def get_contact_name(issue, group_by="assignee"):
    """Extract the display name for the given grouping field."""
    f = issue["fields"]
    if group_by == "qa_contact":
        contact = f.get(QA_CONTACT_FIELD)
        if contact:
            if isinstance(contact, dict):
                return contact.get("displayName", contact.get("emailAddress", "Unknown"))
            return str(contact)
        return "No QA Contact"
    assignee = f.get("assignee")
    return assignee["displayName"] if assignee else "Unassigned"


def generate_markdown(version, issues, total, qe_mode=False, subtasks_by_parent=None):
    group_by = "qa_contact" if qe_mode else "assignee"
    group_label = "QA Contact" if qe_mode else "Assignee"

    by_type = defaultdict(list)
    for issue in issues:
        itype = issue["fields"].get("issuetype", {}).get("name", "Other")
        by_type[itype].append(issue)

    all_contacts = set()
    for issue in issues:
        all_contacts.add(get_contact_name(issue, group_by))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if qe_mode:
        included = ", ".join(QE_STATUSES)
        jql = build_qe_jql(version)
        title = f"{version} QE Report ({included})"
    else:
        excluded = ", ".join(EXCLUDED_STATUSES)
        jql = build_jql(version, EXCLUDED_STATUSES)
        title = f"{version} Issues (Excluding {excluded})"

    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"**JQL:** `{jql}`")
    lines.append("")
    lines.append(f"**Total issues:** {total}  ")
    lines.append(f"**{group_label}s:** {len(all_contacts)}  ")
    lines.append(f"**Generated:** {now}")
    lines.append("")
    lines.append("---")
    lines.append("")

    type_order = sorted(by_type.keys(), key=lambda t: ISSUE_TYPE_ORDER.get(t, 99))

    def slug(text):
        return text.lower().replace(" ", "-").replace("(", "").replace(")", "")

    by_person = defaultdict(lambda: defaultdict(list))
    for issue in issues:
        name = get_contact_name(issue, group_by)
        itype = issue["fields"].get("issuetype", {}).get("name", "Other")
        by_person[name][itype].append(issue)

    all_names = sorted(all_contacts, key=str.lower)
    type_headers = [f"{t}s ({len(by_type[t])})" for t in type_order]

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| {group_label} | " + " | ".join(type_headers) + " | Total |")
    lines.append("|----------|" + "|".join(["-------"] * len(type_order)) + "|-------|")
    for name in all_names:
        cols = []
        row_total = 0
        for itype in type_order:
            count = len(by_person[name].get(itype, []))
            row_total += count
            if count:
                anchor = slug(f"{name}")
                cols.append(f"[{count}](#{anchor})")
            else:
                cols.append("—")
        cols.append(f"**{row_total}**")
        lines.append(f"| {name} | " + " | ".join(cols) + " |")
    totals_row = [f"**{len(by_type[t])}**" for t in type_order]
    totals_row.append(f"**{total}**")
    lines.append(f"| **Total** | " + " | ".join(totals_row) + " |")
    lines.append("")
    lines.append("---")

    subtasks_by_parent = subtasks_by_parent or {}

    for name in all_names:
        person_total = sum(len(v) for v in by_person[name].values())
        lines.append("")
        lines.append(f"# {name} ({person_total})")

        for itype in type_order:
            type_issues = by_person[name].get(itype, [])
            if not type_issues:
                continue
            type_issues.sort(key=lambda i: (
                PRIORITY_ORDER.get(i["fields"].get("priority", {}).get("name", "Undefined"), 99),
                i["fields"]["created"],
            ))
            lines.append("")
            lines.append(f"## {itype}s ({len(type_issues)})")

            if qe_mode:
                for issue in type_issues:
                    f = issue["fields"]
                    key = issue["key"]
                    summary = f["summary"]
                    priority = f.get("priority", {}).get("name", "Undefined")
                    status = f.get("status", {}).get("name", "")
                    link = f"https://{JIRA_SITE}/browse/{key}"
                    lines.append("")
                    lines.append(f"### [{key}]({link}) — {summary}")
                    lines.append(f"**Priority:** {priority} | **Status:** {status}")

                    children = subtasks_by_parent.get(key, [])
                    if children:
                        lines.append("")
                        lines.append("**Platform Validation Tasks:**")
                        lines.append("")
                        lines.append("| Task | Summary | Assignee | Status |")
                        lines.append("|------|---------|----------|--------|")
                        for child in children:
                            cf = child["fields"]
                            ckey = child["key"]
                            clink = f"https://{JIRA_SITE}/browse/{ckey}"
                            csummary = cf.get("summary", "")
                            cassignee = (cf.get("assignee") or {}).get("displayName", "Unassigned")
                            cstatus = (cf.get("status") or {}).get("name", "")
                            lines.append(f"| [{ckey}]({clink}) | {csummary} | {cassignee} | {cstatus} |")
                    else:
                        lines.append("")
                        lines.append("_No subtasks found._")
            else:
                lines.append("")
                lines.append("| Key | Summary | Priority | Status | Created | Labels |")
                lines.append("|-----|---------|----------|--------|---------|--------|")
                for issue in type_issues:
                    lines.append(format_issue_row(issue))

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate OADP bug report from Jira")
    parser.add_argument("--version", "-v", default=DEFAULT_VERSION, help="fixVersion to query")
    parser.add_argument("--output", "-o", default=None,
                        help="output markdown file (default: output/<version>-bugs.md)")
    parser.add_argument("--qe", action="store_true",
                        help="QE report: show ON_QA/VERIFIED issues grouped by QA Contact")
    args = parser.parse_args()

    if args.output is None:
        version_slug = args.version.lower().replace(" ", "-")
        suffix = "qe" if args.qe else "bugs"
        args.output = os.path.join(OUTPUT_DIR, f"{version_slug}-{suffix}.md")

    auth = get_auth_header()
    extra_fields = None

    if args.qe:
        jql = build_qe_jql(args.version)
        extra_fields = [QA_CONTACT_FIELD]
    else:
        jql = build_jql(args.version, EXCLUDED_STATUSES)

    print(f"Querying Jira: {jql}", file=sys.stderr)
    issues, total = jira_search(jql, auth, extra_fields=extra_fields)
    print(f"Found {total} issues", file=sys.stderr)

    subtasks_by_parent = {}
    if args.qe and issues:
        parent_keys = [i["key"] for i in issues]
        print(f"Fetching subtasks for {len(parent_keys)} issues...", file=sys.stderr)
        subtasks_by_parent = fetch_child_issues(parent_keys, auth)
        child_count = sum(len(v) for v in subtasks_by_parent.values())
        print(f"Found {child_count} subtasks across {len(subtasks_by_parent)} parents", file=sys.stderr)

    md = generate_markdown(args.version, issues, total, qe_mode=args.qe,
                           subtasks_by_parent=subtasks_by_parent)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        f.write(md)
    print(f"Wrote {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
