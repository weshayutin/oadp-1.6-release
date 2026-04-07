# OADP 1.6.0 Bugs (Excluding MODIFIED, Closed)

**JQL:** `project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype = Bug AND status not in (MODIFIED, Closed) ORDER BY priority DESC, created DESC`

**Total issues:** 18  
**Assignees:** 7  
**Generated:** 2026-04-07

---

## Joseph Antony Vaikath (2 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-3378](https://redhat.atlassian.net/browse/OADP-3378) | Wrong/ misleading certificate error log for backup when certificate check is disabled | Normal | New | 2024-01-23 | cee.neXT, oadp_encryption, triaged |
| [OADP-3692](https://redhat.atlassian.net/browse/OADP-3692) | Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Minor | ASSIGNED | 2024-03-08 | oadp_crd_api_version_bump, triaged |

## Michal Pryc (2 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5114](https://redhat.atlassian.net/browse/OADP-5114) | Incompatibility of OADP with data mover restore | Normal | POST | 2024-10-25 | oadp_datamover, oadp_upstream_bug_fix, triaged |
| [OADP-6752](https://redhat.atlassian.net/browse/OADP-6752) | Missing .storageconfig file in the backuprepository location on the s3 bsl | Undefined | New | 2025-09-25 | triaged |

## Prasad Joshi (1 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-7673](https://redhat.atlassian.net/browse/OADP-7673) | CLONE - DPA goes in error state when node affinity is specified with podConfig | Major | POST | 2026-03-31 | oadp_operator_improvements, triaged |

## Scott Seago (1 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-5486](https://redhat.atlassian.net/browse/OADP-5486) | Handle - Retry Generate Name | Normal | New | 2025-01-14 | oadp_kube_enhancement, triaged |

## Shubham Dilip Pampattiwar (7 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6699](https://redhat.atlassian.net/browse/OADP-6699) | Ignore OVN-K and multus annotations while backing-up/restoring pods | Blocker | New | 2025-09-18 | triaged |
| [OADP-4743](https://redhat.atlassian.net/browse/OADP-4743) | DataMover restore partially fails when node selector spec is used | Critical | POST | 2024-08-27 | oadp_datamover, oadp_upstream_bug_fix, triaged |
| [OADP-7381](https://redhat.atlassian.net/browse/OADP-7381) | [CSI] VGS restore fails when used with Ceph RBD storage class  | Critical | POST | 2026-02-02 |  |
| [OADP-6880](https://redhat.atlassian.net/browse/OADP-6880) | VolumeGroupSnapshots doesn't respect volumePolicies | Major | POST | 2025-10-20 | oadp_upstream_bug_fix, triaged |
| [OADP-6879](https://redhat.atlassian.net/browse/OADP-6879) | Volume policy is in low performance when there are lots of pods and PVCs in the cluster | Normal | POST | 2025-10-20 | oadp_upstream_bug_fix, triaged |
| [OADP-5171](https://redhat.atlassian.net/browse/OADP-5171) | BSL status.message field shouldn't have the http response as output when bucket doesn't exist | Minor | POST | 2024-11-04 | oadp_bsl, oadp_upstream_bug_fix, triaged |
| [OADP-6740](https://redhat.atlassian.net/browse/OADP-6740) | [Upstream testing] VolumeSnapshotContent resources are left out in cluster with VGS path | Undefined | New | 2025-09-25 | oadp_upstream_bug_fix, triaged |

## Tiger Kaovilai (4 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-6896](https://redhat.atlassian.net/browse/OADP-6896) | Node agent pod restarts cancel all DataUploads across all nodes, blocking backup queue in OADP 1.5 | Major | New | 2025-10-23 | oadp_upstream_bug_fix, oadp_upstream_milestone_v1.18, triaged |
| [OADP-5729](https://redhat.atlassian.net/browse/OADP-5729) | FSBackup doesn't restore ImageStreamTag | Minor | New | 2025-02-28 |  |
| [OADP-5777](https://redhat.atlassian.net/browse/OADP-5777) | Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Undefined | POST | 2025-03-10 | oadp_dpa, triaged |
| [OADP-5829](https://redhat.atlassian.net/browse/OADP-5829) | wrong S3 identifier (resticIdentifier) while using a kopia BackupRepository  | Undefined | POST | 2025-03-20 | oadp_upstream_bug_fix |

## Wesley Hayutin (1 issues)

| Key | Summary | Priority | Status | Created | Labels |
|-----|---------|----------|--------|---------|--------|
| [OADP-3039](https://redhat.atlassian.net/browse/OADP-3039) | PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Normal | POST | 2023-11-03 | oadp_upstream_bug_fix, oadp_validation, triaged |
