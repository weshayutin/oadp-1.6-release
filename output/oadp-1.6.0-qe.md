# OADP 1.6.0 QE Report (ON_QA)

**JQL:** `project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic) AND status in ("ON_QA") ORDER BY priority DESC, created DESC`

**Total issues:** 23  
**QA Contacts:** 7  
**Generated:** 2026-04-20

---

## Navigation

| QA Contact | Bugs (23) | Total |
|----------|-------|-------|
| Aziza Karol | [5](#aziza-karol-5) | **5** |
| David Vaanunu | [1](#david-vaanunu-1) | **1** |
| Md Nadeem | [5](#md-nadeem-5) | **5** |
| Prasad Joshi | [4](#prasad-joshi-4) | **4** |
| Pratik Mane | [5](#pratik-mane-5) | **5** |
| Tareq Alayan | [2](#tareq-alayan-2) | **2** |
| Wesley Hayutin | [1](#wesley-hayutin-1) | **1** |
| **Total** | **23** | **23** |

---

# Bugs (23)

## Aziza Karol (5)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6764](https://redhat.atlassian.net/browse/OADP-6764) | Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path | Critical | ON_QA | 2025-09-26 | filesystem-backup, need-rh-and-ibm-qe, oadp_upstream_bug_fix, openshift, privileged-context, triaged, upstream |
| [OADP-6955](https://redhat.atlassian.net/browse/OADP-6955) | Fix the Job build error when BackupRepository name longer than 63 | Critical | ON_QA | 2025-10-30 | need-rh-and-ibm-qe, oadp_upstream_bug_fix, rosa-impact, triaged |
| [OADP-6911](https://redhat.atlassian.net/browse/OADP-6911) | [Upstream] Restore CR Completed while PodVolumeRestore CR is InProgress | Major | ON_QA | 2025-10-27 | oadp_upstream_bug_fix, triaged, upstream |
| [OADP-7382](https://redhat.atlassian.net/browse/OADP-7382) | NonAdminController reports reconciler error due to new backup phases  | Major | ON_QA | 2026-02-02 | need-rh-and-ibm-qe, triaged |
| [OADP-3378](https://redhat.atlassian.net/browse/OADP-3378) | Wrong/ misleading certificate error log for backup when certificate check is disabled | Normal | ON_QA | 2024-01-23 | cee.neXT, need-rh-and-ibm-qe, oadp_encryption, triaged |

## David Vaanunu (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-4855](https://redhat.atlassian.net/browse/OADP-4855) | Kopia leaving cache on worker node | Blocker | ON_QA | 2024-09-13 | Scale&Perf-QE, oadp_kopia, oadp_upstream_bug_fix, triaged |

## Md Nadeem (5)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-4668](https://redhat.atlassian.net/browse/OADP-4668) | Make using Velero CLI via velero deployment with caCert simple. | Critical | ON_QA | 2024-08-07 | oadp_cli, triaged |
| [OADP-6896](https://redhat.atlassian.net/browse/OADP-6896) | Node agent pod restarts cancel all DataUploads across all nodes, blocking backup queue in OADP 1.5 | Major | ON_QA | 2025-10-23 | oadp_upstream_bug_fix, oadp_upstream_milestone_v1.18, rosa-impact, triaged |
| [OADP-6879](https://redhat.atlassian.net/browse/OADP-6879) | Volume policy is in low performance when there are lots of pods and PVCs in the cluster | Normal | ON_QA | 2025-10-20 | oadp_upstream_bug_fix, triaged |
| [OADP-5829](https://redhat.atlassian.net/browse/OADP-5829) | wrong S3 identifier (resticIdentifier) while using a kopia BackupRepository  | Undefined | ON_QA | 2025-03-20 | oadp_upstream_bug_fix, triaged |
| [OADP-7132](https://redhat.atlassian.net/browse/OADP-7132) | openshift-velero-plugin panics with 'concurrent map writes' | Undefined | ON_QA | 2025-12-16 | customer-bug, customer-case, triaged |

## Prasad Joshi (4)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6699](https://redhat.atlassian.net/browse/OADP-6699) | Ignore OVN-K and multus annotations while backing-up/restoring pods | Blocker | ON_QA | 2025-09-18 | triaged |
| [OADP-4743](https://redhat.atlassian.net/browse/OADP-4743) | DataMover restore partially fails when node selector spec is used | Critical | ON_QA | 2024-08-27 | need-rh-and-ibm-qe, oadp_datamover, oadp_upstream_bug_fix, triaged |
| [OADP-6846](https://redhat.atlassian.net/browse/OADP-6846) | Support for labels/annotations on DataProtectionApplications | Critical | ON_QA | 2025-10-13 | triaged |
| [OADP-7381](https://redhat.atlassian.net/browse/OADP-7381) | [CSI] VGS restore fails when used with Ceph RBD storage class  | Critical | ON_QA | 2026-02-02 | triaged |

## Pratik Mane (5)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-3039](https://redhat.atlassian.net/browse/OADP-3039) | PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Normal | ON_QA | 2023-11-03 | need-rh-and-ibm-qe, oadp_upstream_bug_fix, oadp_validation, triaged |
| [OADP-3759](https://redhat.atlassian.net/browse/OADP-3759) | Velero shouldn't restore the restore-wait init container | Normal | ON_QA | 2024-03-20 | need-rh-and-ibm-qe, oadp_upstream_bug_fix, oadp_validation, triaged, velero_1.17-candidate |
| [OADP-3360](https://redhat.atlassian.net/browse/OADP-3360) | PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Minor | ON_QA | 2024-01-17 | need-rh-and-ibm-qe, oadp_upstream_bug_fix, oadp_upstream_milestone_v1.18, oadp_validation, triaged |
| [OADP-5171](https://redhat.atlassian.net/browse/OADP-5171) | BSL status.message field shouldn't have the http response as output when bucket doesn't exist | Minor | ON_QA | 2024-11-04 | oadp_bsl, oadp_upstream_bug_fix, triaged |
| [OADP-7070](https://redhat.atlassian.net/browse/OADP-7070) | Unable to configure spec.configuration.nodeAgent.loadConcurrency.PrepareQueueLength in DPA | Undefined | ON_QA | 2025-12-09 | oadp_dpa, triaged |

## Tareq Alayan (2)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5114](https://redhat.atlassian.net/browse/OADP-5114) | Incompatibility of OADP with data mover restore | Normal | ON_QA | 2024-10-25 | need-rh-and-ibm-qe, oadp_datamover, oadp_upstream_bug_fix, triaged |
| [OADP-5777](https://redhat.atlassian.net/browse/OADP-5777) | Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Undefined | ON_QA | 2025-03-10 | need-rh-and-ibm-qe, oadp_dpa, oadp_upstream_milestone_v1.18, triaged |

## Wesley Hayutin (1)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6880](https://redhat.atlassian.net/browse/OADP-6880) | VolumeGroupSnapshots doesn't respect volumePolicies | Major | ON_QA | 2025-10-20 | oadp_upstream_bug_fix, triaged |
