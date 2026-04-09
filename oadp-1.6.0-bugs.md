# OADP 1.6.0 Issues (Excluding MODIFIED, Closed)

**JQL:** `project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic) AND status not in (MODIFIED, Closed) ORDER BY priority DESC, created DESC`

**Total issues:** 58  
**Assignees:** 11  
**Generated:** 2026-04-09

---

## Navigation

| Assignee | Bugs (15) | Tasks (33) | Epics (10) | Total |
|----------|-------|-------|-------|-------|
| Andy Arnold | — | [20](#andy-arnold-20) | — | **20** |
| Joseph Antony Vaikath | [1](#joseph-antony-vaikath-1) | [1](#joseph-antony-vaikath-1) | [1](#joseph-antony-vaikath-1) | **3** |
| Michal Pryc | [2](#michal-pryc-2) | — | [2](#michal-pryc-2) | **4** |
| Prasad Joshi | [1](#prasad-joshi-1) | — | — | **1** |
| Scott Seago | — | [2](#scott-seago-2) | [2](#scott-seago-2) | **4** |
| Shruti Deshpande | — | [1](#shruti-deshpande-1) | — | **1** |
| Shubham Dilip Pampattiwar | [7](#shubham-dilip-pampattiwar-7) | — | [2](#shubham-dilip-pampattiwar-2) | **9** |
| Tareq Alayan | — | [6](#tareq-alayan-6) | [1](#tareq-alayan-1) | **7** |
| Tiger Kaovilai | [3](#tiger-kaovilai-3) | — | [1](#tiger-kaovilai-1) | **4** |
| Valentina Ashirova | — | [2](#valentina-ashirova-2) | — | **2** |
| Wesley Hayutin | [1](#wesley-hayutin-1) | [1](#wesley-hayutin-1) | [1](#wesley-hayutin-1) | **3** |
| **Total** | **15** | **33** | **10** | **58** |

---

# Bugs (15)

## Joseph Antony Vaikath (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-3692](https://redhat.atlassian.net/browse/OADP-3692) | Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Minor | ASSIGNED | 2024-03-08 | oadp_crd_api_version_bump, triaged |

## Michal Pryc (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5114](https://redhat.atlassian.net/browse/OADP-5114) | Incompatibility of OADP with data mover restore | Normal | POST | 2024-10-25 | oadp_datamover, oadp_upstream_bug_fix, triaged |
| [OADP-6752](https://redhat.atlassian.net/browse/OADP-6752) | Missing .storageconfig file in the backuprepository location on the s3 bsl | Undefined | New | 2025-09-25 | triaged |

## Prasad Joshi (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7673](https://redhat.atlassian.net/browse/OADP-7673) | CLONE - DPA goes in error state when node affinity is specified with podConfig | Major | POST | 2026-03-31 | oadp_operator_improvements, triaged |

## Shubham Dilip Pampattiwar (7)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6699](https://redhat.atlassian.net/browse/OADP-6699) | Ignore OVN-K and multus annotations while backing-up/restoring pods | Blocker | POST | 2025-09-18 | triaged |
| [OADP-4743](https://redhat.atlassian.net/browse/OADP-4743) | DataMover restore partially fails when node selector spec is used | Critical | POST | 2024-08-27 | oadp_datamover, oadp_upstream_bug_fix, triaged |
| [OADP-7381](https://redhat.atlassian.net/browse/OADP-7381) | [CSI] VGS restore fails when used with Ceph RBD storage class  | Critical | POST | 2026-02-02 | triaged |
| [OADP-6880](https://redhat.atlassian.net/browse/OADP-6880) | VolumeGroupSnapshots doesn't respect volumePolicies | Major | POST | 2025-10-20 | oadp_upstream_bug_fix, triaged |
| [OADP-6879](https://redhat.atlassian.net/browse/OADP-6879) | Volume policy is in low performance when there are lots of pods and PVCs in the cluster | Normal | POST | 2025-10-20 | oadp_upstream_bug_fix, triaged |
| [OADP-5171](https://redhat.atlassian.net/browse/OADP-5171) | BSL status.message field shouldn't have the http response as output when bucket doesn't exist | Minor | POST | 2024-11-04 | oadp_bsl, oadp_upstream_bug_fix, triaged |
| [OADP-6740](https://redhat.atlassian.net/browse/OADP-6740) | [Upstream testing] VolumeSnapshotContent resources are left out in cluster with VGS path | Undefined | New | 2025-09-25 | oadp_upstream_bug_fix, triaged |

## Tiger Kaovilai (3)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5729](https://redhat.atlassian.net/browse/OADP-5729) | FSBackup doesn't restore ImageStreamTag | Minor | New | 2025-02-28 |  |
| [OADP-5777](https://redhat.atlassian.net/browse/OADP-5777) | Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Undefined | POST | 2025-03-10 | oadp_dpa, triaged |
| [OADP-5829](https://redhat.atlassian.net/browse/OADP-5829) | wrong S3 identifier (resticIdentifier) while using a kopia BackupRepository  | Undefined | POST | 2025-03-20 | oadp_upstream_bug_fix |

## Wesley Hayutin (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-3039](https://redhat.atlassian.net/browse/OADP-3039) | PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Normal | POST | 2023-11-03 | oadp_upstream_bug_fix, oadp_validation, triaged |

# Tasks (33)

## Andy Arnold (20)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6316](https://redhat.atlassian.net/browse/OADP-6316) | [DOC] OADP support for single stack IPv6 | Major | New | 2025-06-26 | 4.20, Documentation, OCP, oadp |
| [OADP-6673](https://redhat.atlassian.net/browse/OADP-6673) | [DOC] Parallel backups | Major | New | 2025-09-08 |  |
| [OADP-6708](https://redhat.atlassian.net/browse/OADP-6708) | [DOC] Ignore OVN-K and multus annotations while backing-up/restoring pods | Major | New | 2025-09-22 |  |
| [OADP-6717](https://redhat.atlassian.net/browse/OADP-6717) | [DOC]  VolumeGroupSnapshot Support Implementation | Major | New | 2025-09-24 |  |
| [OADP-6719](https://redhat.atlassian.net/browse/OADP-6719) | Repo cache volume -- Doc change for repo cache volume | Major | New | 2025-09-24 | oadp_upstream_milestone_v1.18, triaged |
| [OADP-6797](https://redhat.atlassian.net/browse/OADP-6797) | [DOC] more than one BSL connected to the same s3 endpoint and velero prefix is NOT supported. | Major | New | 2025-10-02 |  |
| [OADP-6798](https://redhat.atlassian.net/browse/OADP-6798) | Doc: more than one BSL connected to the same s3 endpoint and velero prefix is NOT supported. | Major | New | 2025-10-02 |  |
| [OADP-6818](https://redhat.atlassian.net/browse/OADP-6818) | [DOC] Release notes and attributes OADP 1.6.0  | Major | New | 2025-10-08 |  |
| [OADP-6819](https://redhat.atlassian.net/browse/OADP-6819) | [DOC] OADP install should be cluster scoped, should be able to manage multiple DPA's on cluster | Major | New | 2025-10-08 |  |
| [OADP-6823](https://redhat.atlassian.net/browse/OADP-6823) | [DOC] Add support for adding annotations to PodConfig | Major | New | 2025-10-08 |  |
| [OADP-6920](https://redhat.atlassian.net/browse/OADP-6920) | [DOC] Add possibility to configure "priorityClassName" for node-agent daemons | Major | New | 2025-10-27 |  |
| [OADP-7057](https://redhat.atlassian.net/browse/OADP-7057) | [DOC] VMFR (VM Single File Restore)  (CNV) | Major | New | 2025-12-05 |  |
| [OADP-7058](https://redhat.atlassian.net/browse/OADP-7058) | [DOC] VMDR (Virtual Machine Data Protection) / Kopia client on VM (CNV) | Major | New | 2025-12-05 |  |
| [OADP-7059](https://redhat.atlassian.net/browse/OADP-7059) | [DOC] Incremental backups for VM (CNV) | Major | New | 2025-12-05 |  |
| [OADP-7483](https://redhat.atlassian.net/browse/OADP-7483) | [DOC] Issue with OADP docs navigation | Major | Testing | 2026-02-19 |  |
| [OADP-6503](https://redhat.atlassian.net/browse/OADP-6503) | [DOC] Improve introduction to clarify purpose of OADP | Normal | New | 2025-08-07 | ContentX_CY25, to-be-triaged |
| [OADP-6504](https://redhat.atlassian.net/browse/OADP-6504) | [DOC] Improve linkage to other products  | Normal | New | 2025-08-07 | ContentX_CY25, to-be-triaged |
| [OADP-7060](https://redhat.atlassian.net/browse/OADP-7060) | [DOC] Improve Overriding Kopia hashing, encryption, and splitter algorithms docs | Normal | New | 2025-12-05 |  |
| [OADP-7076](https://redhat.atlassian.net/browse/OADP-7076) | [DOC] Impossible Cloud to be added as a supported S3-compatible backup storage provider | Normal | New | 2025-12-10 |  |
| [OADP-7697](https://redhat.atlassian.net/browse/OADP-7697) | [Documentation for]  Concurrent Backup Processing Implementation | Undefined | New | 2026-04-08 |  |

## Joseph Antony Vaikath (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6073](https://redhat.atlassian.net/browse/OADP-6073) | [OADP] Evaluate Readiness Requirements for PQC | Major | In Progress | 2025-05-05 | 4.20-candidate, o, oadp, oadp_pm_request, triaged |

## Scott Seago (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-4589](https://redhat.atlassian.net/browse/OADP-4589) | Dataupload object reporting improvements | Major | Dev Complete | 2024-07-25 | triaged |
| [OADP-6478](https://redhat.atlassian.net/browse/OADP-6478) | Revert selective PVC restore by label PR before rebase after upstream velero  | Undefined | New | 2025-07-30 | oadp_rebase, traiged |

## Shruti Deshpande (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7690](https://redhat.atlassian.net/browse/OADP-7690) | [DOC] - New BSL default needs DPA restart | Normal | New | 2026-04-07 | Scale&Perf-QE, triaged |

## Tareq Alayan (6)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5160](https://redhat.atlassian.net/browse/OADP-5160) | (QE) [OADP 1.6.0] Review tickets for OADP 1.6.0 | Undefined | New | 2024-10-31 |  |
| [OADP-5161](https://redhat.atlassian.net/browse/OADP-5161) | (QE) [OADP 1.6.0] Test matrix ran and passed  | Undefined | New | 2024-10-31 |  |
| [OADP-5162](https://redhat.atlassian.net/browse/OADP-5162) | (QE) [OADP 1.6.0] Make sure to deploy oadp using UI | Undefined | New | 2024-10-31 |  |
| [OADP-5163](https://redhat.atlassian.net/browse/OADP-5163) | (QE) [OADP 1.6.0] Run the tests when oadp is pushed to production | Undefined | New | 2024-10-31 |  |
| [OADP-5164](https://redhat.atlassian.net/browse/OADP-5164) | (QE) [OADP 1.6.0] Run the tests when oadp is pushed to STAGING | Undefined | New | 2024-10-31 |  |
| [OADP-5165](https://redhat.atlassian.net/browse/OADP-5165) | (QE) [OADP 1.6.0] Push to REL_PREP  | Undefined | New | 2024-10-31 |  |

## Valentina Ashirova (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-2425](https://redhat.atlassian.net/browse/OADP-2425) | Document OADP NFS plugin for full NFS support | Major | New | 2023-08-20 |  |
| [OADP-7028](https://redhat.atlassian.net/browse/OADP-7028) | [DOC] OADP 1.5 Release Notes DITA error | Normal | Testing | 2025-11-26 | CQA, CQreview_non-negotiable, CQreview_pre-migration, content-strategy, dita-error |

## Wesley Hayutin (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6138](https://redhat.atlassian.net/browse/OADP-6138) | (not doc) Kopia repository options settings | Normal | New | 2025-05-15 | Kopia, authentication-client, data-compression, dpa, encryption, feature-enhancement, future_feature |

# Epics (10)

## Joseph Antony Vaikath (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6544](https://redhat.atlassian.net/browse/OADP-6544) | kubectl-oadp CLI Plugin Implementation | Blocker | In Progress | 2025-08-15 | need-qe-and-doc |

## Michal Pryc (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6864](https://redhat.atlassian.net/browse/OADP-6864) | Virtual Machine File Restore - Kubernetes-native solution for recovering individual files from KubeVirt VM backups | Blocker | In Progress | 2025-10-15 | need-qe-and-doc |
| [OADP-6583](https://redhat.atlassian.net/browse/OADP-6583) | OADP Virtual Machine Data Protection (VMDP) Implementation | Undefined | In Progress | 2025-08-15 | need-qe-and-doc, oadp_cnv, triaged |

## Scott Seago (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6579](https://redhat.atlassian.net/browse/OADP-6579) | Concurrent Backup Processing Implementation | Blocker | In Progress | 2025-08-15 | need-qe-and-doc, oadp_parallel_backup, oadp_upstream_bug_fix, triaged |
| [OADP-6584](https://redhat.atlassian.net/browse/OADP-6584) | Support for Storage Agnostic qcow2 Incremental Backup | Critical | In Progress | 2025-08-15 | oadp_cnv, triaged |

## Shubham Dilip Pampattiwar (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6581](https://redhat.atlassian.net/browse/OADP-6581) | VolumeGroupSnapshot Support Implementation | Blocker | In Progress | 2025-08-15 | need-qe-and-doc, oadp_upstream_bug_fix, oadp_vgs, triaged |
| [OADP-7194](https://redhat.atlassian.net/browse/OADP-7194) | Add OADP Toolset to OpenShift MCP Server | Major | In Progress | 2026-01-06 | FPC:TODO-Close-ALL-Epics, FPC:TODO-Create-Delivery-Epics, applied-ai, oadp_pm_request |

## Tareq Alayan (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5159](https://redhat.atlassian.net/browse/OADP-5159) | (QE) OADP-OADP 1.6.0 release activities | Undefined | New | 2024-10-31 |  |

## Tiger Kaovilai (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7417](https://redhat.atlassian.net/browse/OADP-7417) | Scrub oadp / velero code for TLS Config | Blocker | New | 2026-02-03 | oadp_upstream_bug_fix, triaged |

## Wesley Hayutin (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6580](https://redhat.atlassian.net/browse/OADP-6580) | OADP 1.6.0 Release Epic, released with >= OCP 4.22 | Critical | New | 2025-08-15 | rosa-impact |
