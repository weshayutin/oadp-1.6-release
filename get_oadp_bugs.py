#!/usr/bin/env python3
"""
Query OADP Jira bugs for a given fixVersion and generate a markdown report
grouped by assignee.

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
    fields = "summary,status,priority,created,labels,assignee"
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


def build_jql(version, excluded_statuses):
    statuses = ", ".join(excluded_statuses)
    return (
        f'project = OADP AND fixVersion = "{version}" AND issuetype = Bug '
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
    by_assignee = defaultdict(list)
    for issue in issues:
        assignee = issue["fields"].get("assignee")
        name = assignee["displayName"] if assignee else "Unassigned"
        by_assignee[name].append(issue)

    assignee_names = sorted(by_assignee.keys(), key=str.lower)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    excluded = ", ".join(EXCLUDED_STATUSES)
    jql = build_jql(version, EXCLUDED_STATUSES)

    lines = []
    lines.append(f"# {version} Bugs (Excluding {excluded})")
    lines.append("")
    lines.append(f"**JQL:** `{jql}`")
    lines.append("")
    lines.append(f"**Total issues:** {total}  ")
    lines.append(f"**Assignees:** {len(by_assignee)}  ")
    lines.append(f"**Generated:** {now}")
    lines.append("")
    lines.append("---")

    for name in assignee_names:
        issues_for = by_assignee[name]
        issues_for.sort(key=lambda i: (
            PRIORITY_ORDER.get(i["fields"].get("priority", {}).get("name", "Undefined"), 99),
            i["fields"]["created"],
        ))
        lines.append("")
        lines.append(f"## {name} ({len(issues_for)} issues)")
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
