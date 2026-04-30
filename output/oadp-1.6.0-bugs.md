# OADP 1.6.0 Issues (Excluding MODIFIED, Closed, ON_QA, Dev Complete, Verified)

**JQL:** `((project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic) AND status not in ("MODIFIED", "Closed", "ON_QA", "Dev Complete", "Verified")) OR (project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype = Story AND status in ("New", "To Do", "In Progress"))) AND component != "Documentation" ORDER BY priority DESC, created DESC`

**Total issues:** 11  
**Assignees:** 5  
**Generated:** 2026-04-30

---

## Summary

| Assignee | Bugs (1) | Tasks (7) | Epics (2) | Storys (1) | Total |
|----------|-------|-------|-------|-------|-------|
| Prasad Joshi | — | — | — | [1](#prasad-joshi) | **1** |
| Scott Seago | — | [1](#scott-seago) | — | — | **1** |
| Shubham Dilip Pampattiwar | — | — | [1](#shubham-dilip-pampattiwar) | — | **1** |
| Tareq Alayan | — | [6](#tareq-alayan) | [1](#tareq-alayan) | — | **7** |
| Tiger Kaovilai | [1](#tiger-kaovilai) | — | — | — | **1** |
| **Total** | **1** | **7** | **2** | **1** | **11** |

---

# Prasad Joshi (1)

## Storys (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7873](https://redhat.atlassian.net/browse/OADP-7873) | (QE) (jira-auto) Automation Failure & skipped Analysis 1.6.0-202604232357 and Update RP | Undefined | In Progress | 2026-04-27 |  |

# Scott Seago (1)

## Tasks (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-4589](https://redhat.atlassian.net/browse/OADP-4589) | Dataupload object reporting improvements | Major | Testing | 2024-07-25 | triaged |

# Shubham Dilip Pampattiwar (1)

## Epics (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7194](https://redhat.atlassian.net/browse/OADP-7194) | Add OADP Toolset to OpenShift MCP Server | Major | In Progress | 2026-01-06 | applied-ai, oadp_pm_request, triaged |

# Tareq Alayan (7)

## Tasks (6)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5160](https://redhat.atlassian.net/browse/OADP-5160) | (QE) [OADP 1.6.0] Review tickets for OADP 1.6.0 | Undefined | New | 2024-10-31 |  |
| [OADP-5161](https://redhat.atlassian.net/browse/OADP-5161) | (QE) [OADP 1.6.0] Test matrix ran and passed  | Undefined | New | 2024-10-31 |  |
| [OADP-5162](https://redhat.atlassian.net/browse/OADP-5162) | (QE) [OADP 1.6.0] Make sure to deploy oadp using UI | Undefined | New | 2024-10-31 |  |
| [OADP-5163](https://redhat.atlassian.net/browse/OADP-5163) | (QE) [OADP 1.6.0] Run the tests when oadp is pushed to production | Undefined | New | 2024-10-31 |  |
| [OADP-5164](https://redhat.atlassian.net/browse/OADP-5164) | (QE) [OADP 1.6.0] Run the tests when oadp is pushed to STAGING | Undefined | New | 2024-10-31 |  |
| [OADP-5165](https://redhat.atlassian.net/browse/OADP-5165) | (QE) [OADP 1.6.0] Push to REL_PREP  | Undefined | New | 2024-10-31 |  |

## Epics (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5159](https://redhat.atlassian.net/browse/OADP-5159) | (QE) OADP-OADP 1.6.0 release activities | Undefined | In Progress | 2024-10-31 |  |

# Tiger Kaovilai (1)

## Bugs (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5777](https://redhat.atlassian.net/browse/OADP-5777) | Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Undefined | POST | 2025-03-10 | need-rh-and-ibm-qe, oadp_dpa, oadp_upstream_milestone_v1.18, triaged |
