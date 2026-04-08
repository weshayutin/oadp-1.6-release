#!/usr/bin/env python3
"""
Fetch the latest available Go builds from:
  - Red Hat buildroots grid: https://dbenoit.pages.redhat.com/grid/buildroots.json
  - Konveyor builder images: https://quay.io/repository/konveyor/builder
"""

import json
import re
import sys
import urllib.request
from collections import defaultdict

BUILDROOTS_URL = "https://dbenoit.pages.redhat.com/grid/buildroots.json"
KONVEYOR_API = "https://quay.io/api/v1/repository/konveyor/builder/tag/"
NUM_VERSIONS = 3  # show latest N minor versions


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "golang-build-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def fetch_rhel_by_minor():
    """Return dict of { '1.25': [entries...], ... } from RHEL buildroots."""
    data = fetch_json(BUILDROOTS_URL)
    by_minor = defaultdict(list)
    for entry in data["Buildroots"]:
        if not entry.get("Target", "").startswith("rhaos-"):
            continue
        m = re.search(r"golang-(\d+)\.(\d+)\.(\d+)", entry["Current"])
        if not m:
            continue
        minor = int(m.group(2))
        by_minor[minor].append(entry)
    return by_minor


def fetch_konveyor_by_minor():
    """Return dict of { 25: [entries...], ... } from quay.io Konveyor builder tags."""
    page, all_tags = 1, []
    while True:
        data = fetch_json(f"{KONVEYOR_API}?limit=100&onlyActiveTags=true&page={page}")
        tags = data.get("tags", [])
        if not tags:
            break
        all_tags.extend(tags)
        if not data.get("has_additional"):
            break
        page += 1

    ver_re = re.compile(r"^(?:(ubi\d+)-)?v(\d+)\.(\d+)\.(\d+)$")
    by_minor = defaultdict(list)
    for tag in all_tags:
        m = ver_re.match(tag["name"])
        if not m:
            continue
        ubi = m.group(1)
        major, minor, patch = int(m.group(2)), int(m.group(3)), int(m.group(4))
        by_minor[minor].append({
            "tag": tag["name"],
            "version": f"{major}.{minor}.{patch}",
            "ubi": ubi or "ubi9",
            "modified": tag.get("last_modified", "N/A"),
            "sort_key": (major, minor, patch, ubi or ""),
        })
    return by_minor


def md_rhel_table(entries):
    if not entries:
        return "_none_\n"
    lines = []
    lines.append("| Target | Current | Latest Brew | Status | Latest Tested |")
    lines.append("|--------|---------|-------------|--------|---------------|")
    for e in sorted(entries, key=lambda x: x["Target"]):
        status = e["LatestBrewStatus"]
        badge = f"**{status}**" if status == "Pass" else status
        lines.append(
            f"| `{e['Target']}` | `{e['Current']}` | `{e['LatestBrew']}` | {badge} | `{e['LatestTested']}` |"
        )
    return "\n".join(lines) + "\n"


def md_konveyor_table(entries):
    if not entries:
        return "_none_\n"
    entries = sorted(entries, key=lambda x: x["sort_key"], reverse=True)
    lines = []
    lines.append("| Tag | Go Version | Base | Last Modified |")
    lines.append("|-----|------------|------|---------------|")
    for e in entries:
        lines.append(f"| `{e['tag']}` | {e['version']} | {e['ubi']} | {e['modified']} |")
    return "\n".join(lines) + "\n"


def main():
    from datetime import datetime, timezone

    errors = []

    try:
        rhel = fetch_rhel_by_minor()
    except Exception as exc:
        errors.append(f"RHEL buildroots: {exc}")
        rhel = {}

    try:
        konveyor = fetch_konveyor_by_minor()
    except Exception as exc:
        errors.append(f"Konveyor tags: {exc}")
        konveyor = {}

    all_minors = set(rhel) | set(konveyor)
    if not all_minors:
        print("ERROR: no data retrieved.", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    latest_minor = max(all_minors)
    show_minors = sorted(
        [m for m in all_minors if m >= latest_minor - (NUM_VERSIONS - 1)],
        reverse=True,
    )

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    out = []
    out.append(f"# Golang Builders — RHEL & Konveyor")
    out.append(f"")
    out.append(f"> Go 1.{show_minors[0]} .. 1.{show_minors[-1]} (latest {NUM_VERSIONS} minor releases) | Generated {now}")
    out.append(f">")
    out.append(f"> Sources: [RHEL Buildroots Grid]({BUILDROOTS_URL}) · [Konveyor Builder](https://quay.io/repository/konveyor/builder?tab=tags)")

    for minor in show_minors:
        ver_label = f"1.{minor}"
        rhel_entries = rhel.get(minor, [])
        konveyor_entries = konveyor.get(minor, [])

        out.append(f"")
        out.append(f"---")
        out.append(f"")
        out.append(f"## Go {ver_label}")
        out.append(f"")
        out.append(f"### RHEL Buildroots ({len(rhel_entries)} targets)")
        out.append(f"")
        out.append(md_rhel_table(rhel_entries))
        out.append(f"### Konveyor Builder — `quay.io/konveyor/builder` ({len(konveyor_entries)} tags)")
        out.append(f"")
        out.append(md_konveyor_table(konveyor_entries))

    if errors:
        out.append(f"---")
        out.append(f"")
        out.append(f"**Warnings:**")
        for e in errors:
            out.append(f"- {e}")

    print("\n".join(out))


if __name__ == "__main__":
    main()
