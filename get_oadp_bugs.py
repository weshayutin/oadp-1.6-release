#!/usr/bin/env python3
"""
Query OADP Jira issues (Bugs, Tasks, Epics) for a given fixVersion and
generate a markdown report grouped by issue type, then by assignee.

Auth: set JIRA_EMAIL and JIRA_API_TOKEN env vars, or create a ~/.netrc entry
for redhat.atlassian.net.

Usage:
    python3 get_oadp_bugs.py                          # defaults to OADP 1.6.0
    python3 get_oadp_bugs.py --version "OADP 1.5.0"
    python3 get_oadp_bugs.py -o oadp-1.6.0-bugs.md   # write to file
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

JIRA_SITE = "redhat.atlassian.net"
API_BASE = f"https://{JIRA_SITE}/rest/api/3"
DEFAULT_VERSION = "OADP 1.6.0"
EXCLUDED_STATUSES = ("MODIFIED", "Closed")
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


def jira_search(jql, auth_header):
    """Return all matching issues, handling pagination via nextPageToken."""
    issues = []
    fields = "summary,status,priority,created,labels,assignee,issuetype"
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


ISSUE_TYPES = ("Bug", "Task", "Epic")
ISSUE_TYPE_ORDER = {t: i for i, t in enumerate(ISSUE_TYPES)}


def build_jql(version, excluded_statuses, issue_types=ISSUE_TYPES):
    statuses = ", ".join(excluded_statuses)
    types = ", ".join(issue_types)
    return (
        f'project = OADP AND fixVersion = "{version}" AND issuetype in ({types}) '
        f"AND status not in ({statuses}) "
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


def generate_markdown(version, issues, total):
    by_type = defaultdict(list)
    for issue in issues:
        itype = issue["fields"].get("issuetype", {}).get("name", "Other")
        by_type[itype].append(issue)

    all_assignees = set()
    for issue in issues:
        assignee = issue["fields"].get("assignee")
        all_assignees.add(assignee["displayName"] if assignee else "Unassigned")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    excluded = ", ".join(EXCLUDED_STATUSES)
    jql = build_jql(version, EXCLUDED_STATUSES)

    lines = []
    lines.append(f"# {version} Issues (Excluding {excluded})")
    lines.append("")
    lines.append(f"**JQL:** `{jql}`")
    lines.append("")
    lines.append(f"**Total issues:** {total}  ")
    lines.append(f"**Assignees:** {len(all_assignees)}  ")
    lines.append(f"**Generated:** {now}")
    lines.append("")
    lines.append("---")
    lines.append("")

    type_order = sorted(by_type.keys(), key=lambda t: ISSUE_TYPE_ORDER.get(t, 99))

    def slug(text):
        return text.lower().replace(" ", "-").replace("(", "").replace(")", "")

    # Build per-type assignee data for navigation table
    nav_data = {}
    for itype in type_order:
        by_a = defaultdict(list)
        for issue in by_type[itype]:
            assignee = issue["fields"].get("assignee")
            name = assignee["displayName"] if assignee else "Unassigned"
            by_a[name].append(issue)
        nav_data[itype] = by_a

    all_names = sorted(all_assignees, key=str.lower)
    type_headers = [f"{t}s ({len(by_type[t])})" for t in type_order]

    lines.append("## Navigation")
    lines.append("")
    lines.append("| Assignee | " + " | ".join(type_headers) + " | Total |")
    lines.append("|----------|" + "|".join(["-------"] * len(type_order)) + "|-------|")
    for name in all_names:
        cols = []
        row_total = 0
        for itype in type_order:
            count = len(nav_data[itype].get(name, []))
            row_total += count
            if count:
                anchor = slug(f"{name} {count}")
                section_label = f"{itype}s".lower()
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

    for itype in type_order:
        type_issues = by_type[itype]
        lines.append("")
        lines.append(f"# {itype}s ({len(type_issues)})")

        by_assignee = defaultdict(list)
        for issue in type_issues:
            assignee = issue["fields"].get("assignee")
            name = assignee["displayName"] if assignee else "Unassigned"
            by_assignee[name].append(issue)

        for name in sorted(by_assignee.keys(), key=str.lower):
            issues_for = by_assignee[name]
            issues_for.sort(key=lambda i: (
                PRIORITY_ORDER.get(i["fields"].get("priority", {}).get("name", "Undefined"), 99),
                i["fields"]["created"],
            ))
            lines.append("")
            lines.append(f"## {name} ({len(issues_for)})")
            lines.append("")
            lines.append("| Key | Summary | Priority | Status | Created | Labels |")
            lines.append("|-----|---------|----------|--------|---------|--------|")
            for issue in issues_for:
                lines.append(format_issue_row(issue))

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate OADP bug report from Jira")
    parser.add_argument("--version", "-v", default=DEFAULT_VERSION, help="fixVersion to query")
    parser.add_argument("--output", "-o", default=None, help="output markdown file (default: stdout)")
    args = parser.parse_args()

    auth = get_auth_header()
    jql = build_jql(args.version, EXCLUDED_STATUSES)

    print(f"Querying Jira: {jql}", file=sys.stderr)
    issues, total = jira_search(jql, auth)
    print(f"Found {total} issues", file=sys.stderr)

    md = generate_markdown(args.version, issues, total)

    if args.output:
        with open(args.output, "w") as f:
            f.write(md)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
