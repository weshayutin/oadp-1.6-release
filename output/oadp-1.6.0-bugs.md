# OADP 1.6.0 Issues (Excluding MODIFIED, Closed, ON_QA, Dev Complete)

**JQL:** `(project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic) AND status not in ("MODIFIED", "Closed", "ON_QA", "Dev Complete")) OR (project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype = Story AND status in ("New", "To Do", "In Progress")) ORDER BY priority DESC, created DESC`

**Total issues:** 46  
**Assignees:** 9  
**Generated:** 2026-04-20

---

## Summary

| Assignee | Bugs (3) | Tasks (30) | Epics (9) | Storys (4) | Total |
|----------|-------|-------|-------|-------|-------|
| Andy Arnold | — | [19](#andy-arnold) | — | [3](#andy-arnold) | **22** |
| Joseph Antony Vaikath | [1](#joseph-antony-vaikath) | [1](#joseph-antony-vaikath) | [1](#joseph-antony-vaikath) | — | **3** |
| Michal Pryc | [1](#michal-pryc) | — | [2](#michal-pryc) | — | **3** |
| Scott Seago | — | [2](#scott-seago) | [2](#scott-seago) | — | **4** |
| Shruti Deshpande | — | [1](#shruti-deshpande) | — | — | **1** |
| Shubham Dilip Pampattiwar | [1](#shubham-dilip-pampattiwar) | — | [2](#shubham-dilip-pampattiwar) | [1](#shubham-dilip-pampattiwar) | **4** |
| Tareq Alayan | — | [6](#tareq-alayan) | [1](#tareq-alayan) | — | **7** |
| Valentina Ashirova | — | [1](#valentina-ashirova) | — | — | **1** |
| Wesley Hayutin | — | — | [1](#wesley-hayutin) | — | **1** |
| **Total** | **3** | **30** | **9** | **4** | **46** |

---

# Andy Arnold (22)

## Tasks (19)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6316](https://redhat.atlassian.net/browse/OADP-6316) | [DOC] OADP support for single stack IPv6 | Major | New | 2025-06-26 | 4.20, Documentation, OCP, oadp, triaged |
| [OADP-6673](https://redhat.atlassian.net/browse/OADP-6673) | [DOC] Parallel backups | Major | New | 2025-09-08 |  |
| [OADP-6708](https://redhat.atlassian.net/browse/OADP-6708) | [DOC] Ignore OVN-K and multus annotations while backing-up/restoring pods | Major | New | 2025-09-22 |  |
| [OADP-6717](https://redhat.atlassian.net/browse/OADP-6717) | [DOC]  VolumeGroupSnapshot Support Implementation | Major | New | 2025-09-24 |  |
| [OADP-6719](https://redhat.atlassian.net/browse/OADP-6719) | Repo cache volume -- Doc change for repo cache volume | Major | New | 2025-09-24 | oadp_upstream_milestone_v1.18, triaged |
| [OADP-6797](https://redhat.atlassian.net/browse/OADP-6797) | [DOC] more than one BSL connected to the same s3 endpoint and velero prefix is NOT supported. | Major | New | 2025-10-02 |  |
| [OADP-6818](https://redhat.atlassian.net/browse/OADP-6818) | [DOC] Release notes and attributes OADP 1.6.0  | Major | New | 2025-10-08 |  |
| [OADP-6920](https://redhat.atlassian.net/browse/OADP-6920) | [DOC] Add possibility to configure "priorityClassName" for node-agent daemons | Major | New | 2025-10-27 |  |
| [OADP-7057](https://redhat.atlassian.net/browse/OADP-7057) | [DOC] VMFR (VM Single File Restore)  (CNV) | Major | New | 2025-12-05 |  |
| [OADP-7058](https://redhat.atlassian.net/browse/OADP-7058) | [DOC] VMDR (Virtual Machine Data Protection) / Kopia client on VM (CNV) | Major | New | 2025-12-05 |  |
| [OADP-7059](https://redhat.atlassian.net/browse/OADP-7059) | [DOC] Incremental backups for VM (CNV) | Major | New | 2025-12-05 |  |
| [OADP-7483](https://redhat.atlassian.net/browse/OADP-7483) | [DOC] Issue with OADP docs navigation | Major | Testing | 2026-02-19 |  |
| [OADP-6503](https://redhat.atlassian.net/browse/OADP-6503) | [DOC] Improve introduction to clarify purpose of OADP | Normal | New | 2025-08-07 | ContentX_CY25, to-be-triaged, triaged |
| [OADP-6504](https://redhat.atlassian.net/browse/OADP-6504) | [DOC] Improve linkage to other products  | Normal | New | 2025-08-07 | ContentX_CY25, to-be-triaged, triaged |
| [OADP-7060](https://redhat.atlassian.net/browse/OADP-7060) | [DOC] Improve Overriding Kopia hashing, encryption, and splitter algorithms docs | Normal | New | 2025-12-05 |  |
| [OADP-7076](https://redhat.atlassian.net/browse/OADP-7076) | [DOC] Impossible Cloud to be added as a supported S3-compatible backup storage provider | Normal | New | 2025-12-10 |  |
| [OADP-7697](https://redhat.atlassian.net/browse/OADP-7697) | [Documentation for]  Concurrent Backup Processing Implementation | Undefined | New | 2026-04-08 |  |
| [OADP-7862](https://redhat.atlassian.net/browse/OADP-7862) | [Documentation for]  Virtual Machine File Restore - Kubernetes-native solution for recovering individual files from KubeVirt VM backups | Undefined | New | 2026-04-20 |  |
| [OADP-7866](https://redhat.atlassian.net/browse/OADP-7866) | [Documentation for]  kubectl-oadp CLI Plugin Implementation | Undefined | New | 2026-04-20 |  |

## Storys (3)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6278](https://redhat.atlassian.net/browse/OADP-6278) | [DOC] In-Guest File-Level Backup for the OpenShift KubeVirt VMs via OADP | Major | New | 2025-06-16 | CNV, triaged |
| [OADP-6995](https://redhat.atlassian.net/browse/OADP-6995) | [DOC] kubectl-oadp CLI Plugin Implementation | Major | New | 2025-11-10 |  |
| [OADP-6993](https://redhat.atlassian.net/browse/OADP-6993) | [DOC] Wildcard namespace support | Normal | New | 2025-11-10 | oadp_upstream_milestone_v1.18, triaged |

# Joseph Antony Vaikath (3)

## Bugs (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-3692](https://redhat.atlassian.net/browse/OADP-3692) | Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Minor | ASSIGNED | 2024-03-08 | need-rh-and-ibm-qe, oadp_crd_api_version_bump, triaged |

## Tasks (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6073](https://redhat.atlassian.net/browse/OADP-6073) | [OADP] Evaluate Readiness Requirements for PQC | Major | In Progress | 2025-05-05 | 4.20-candidate, o, oadp, oadp_pm_request, triaged |

## Epics (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6544](https://redhat.atlassian.net/browse/OADP-6544) | kubectl-oadp CLI Plugin Implementation | Blocker | In Progress | 2025-08-15 | need-qe-and-doc, triaged |

# Michal Pryc (3)

## Bugs (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6752](https://redhat.atlassian.net/browse/OADP-6752) | Missing .storageconfig file in the backuprepository location on the s3 bsl | Undefined | New | 2025-09-25 | triaged |

## Epics (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6864](https://redhat.atlassian.net/browse/OADP-6864) | Virtual Machine File Restore - Kubernetes-native solution for recovering individual files from KubeVirt VM backups | Blocker | In Progress | 2025-10-15 | need-qe-and-doc, triaged |
| [OADP-6583](https://redhat.atlassian.net/browse/OADP-6583) | OADP Virtual Machine Data Protection (VMDP) Implementation | Undefined | In Progress | 2025-08-15 | need-qe-and-doc, oadp_cnv, triaged |

# Scott Seago (4)

## Tasks (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-4589](https://redhat.atlassian.net/browse/OADP-4589) | Dataupload object reporting improvements | Major | Testing | 2024-07-25 | triaged |
| [OADP-6478](https://redhat.atlassian.net/browse/OADP-6478) | Revert selective PVC restore by label PR before rebase after upstream velero  | Undefined | New | 2025-07-30 | oadp_rebase, traiged, triaged |

## Epics (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6579](https://redhat.atlassian.net/browse/OADP-6579) | Concurrent Backup Processing Implementation | Blocker | In Progress | 2025-08-15 | need-qe-and-doc, oadp_parallel_backup, oadp_upstream_bug_fix, triaged |
| [OADP-6584](https://redhat.atlassian.net/browse/OADP-6584) | Tech-Preview - Support for Storage Agnostic qcow2 Incremental Backup | Critical | In Progress | 2025-08-15 | oadp_cnv, triaged |

# Shruti Deshpande (1)

## Tasks (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7690](https://redhat.atlassian.net/browse/OADP-7690) | [DOC] - New BSL default needs DPA restart | Normal | In Progress | 2026-04-07 | Scale&Perf-QE, triaged |

# Shubham Dilip Pampattiwar (4)

## Bugs (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6740](https://redhat.atlassian.net/browse/OADP-6740) | [Upstream testing] VolumeSnapshotContent resources are left out in cluster with VGS path | Undefined | New | 2025-09-25 | oadp_upstream_bug_fix, triaged |

## Epics (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6581](https://redhat.atlassian.net/browse/OADP-6581) | Tech-Preview  - VolumeGroupSnapshot Support Implementation | Blocker | In Progress | 2025-08-15 | need-qe-and-doc, oadp_upstream_bug_fix, oadp_vgs, triaged |
| [OADP-7194](https://redhat.atlassian.net/browse/OADP-7194) | Add OADP Toolset to OpenShift MCP Server | Major | In Progress | 2026-01-06 | FPC:TODO-Close-ALL-Epics, FPC:TODO-Create-Delivery-Epics, applied-ai, oadp_pm_request, triaged |

## Storys (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6693](https://redhat.atlassian.net/browse/OADP-6693) | Address sparsify requirement post DM restore on ODF. | Undefined | In Progress | 2025-09-15 | oadp_odf, triaged |

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

# Valentina Ashirova (1)

## Tasks (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-2425](https://redhat.atlassian.net/browse/OADP-2425) | Document OADP NFS plugin for full NFS support | Major | New | 2023-08-20 |  |

# Wesley Hayutin (1)

## Epics (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6580](https://redhat.atlassian.net/browse/OADP-6580) | OADP 1.6.0 Release Epic, released with >= OCP 4.22 | Critical | New | 2025-08-15 | rosa-impact, triaged |
