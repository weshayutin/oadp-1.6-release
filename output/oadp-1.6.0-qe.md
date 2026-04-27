# OADP 1.6.0 QE Report (ON_QA)

**JQL:** `project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic, Story) AND status in ("ON_QA") ORDER BY priority DESC, created DESC`

**Total issues:** 14  
**QA Contacts:** 7  
**Generated:** 2026-04-27

---

## Summary

| QA Contact | Bugs (14) | Total |
|----------|-------|-------|
| Aziza Karol | [3](#aziza-karol) | **3** |
| David Vaanunu | [1](#david-vaanunu) | **1** |
| Md Nadeem | [1](#md-nadeem) | **1** |
| Prasad Joshi | [3](#prasad-joshi) | **3** |
| Pratik Mane | [3](#pratik-mane) | **3** |
| Tareq Alayan | [1](#tareq-alayan) | **1** |
| Wesley Hayutin | [2](#wesley-hayutin) | **2** |
| **Total** | **14** | **14** |

---

# Aziza Karol (3)

## Bugs (3)

### [OADP-6955](https://redhat.atlassian.net/browse/OADP-6955) — Fix the Job build error when BackupRepository name longer than 63
**Priority:** Critical | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7799](https://redhat.atlassian.net/browse/OADP-7799) | [RedHat QE] Verify Bug  OADP-6955 - Fix the Job build error when BackupRepository name longer than 63 | Aziza Karol | Closed |
| [OADP-7800](https://redhat.atlassian.net/browse/OADP-7800) | [IBM QE-P] Verify Bug OADP-6955 - Fix the Job build error when BackupRepository name longer than 63 | Sonia Garudi | Closed |
| [OADP-7801](https://redhat.atlassian.net/browse/OADP-7801) | [IBM QE-Z] Verify Bug OADP-6955 - Fix the Job build error when BackupRepository name longer than 63 | Ukthi Prasad | New |

### [OADP-7382](https://redhat.atlassian.net/browse/OADP-7382) — NonAdminController reports reconciler error due to new backup phases 
**Priority:** Major | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7854](https://redhat.atlassian.net/browse/OADP-7854) | [RedHat QE] Verify Bug  OADP-7382 - NonAdminController reports reconciler error due to new backup phases  | Aziza Karol | Closed |
| [OADP-7856](https://redhat.atlassian.net/browse/OADP-7856) | [IBM QE-P] Verify Bug OADP-7382 - NonAdminController reports reconciler error due to new backup phases  | Sonia Garudi | Closed |
| [OADP-7864](https://redhat.atlassian.net/browse/OADP-7864) | [IBM QE-Z] Verify Bug OADP-7382 - NonAdminController reports reconciler error due to new backup phases  | Ukthi Prasad | Testing |

### [OADP-3378](https://redhat.atlassian.net/browse/OADP-3378) — Wrong/ misleading certificate error log for backup when certificate check is disabled
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7812](https://redhat.atlassian.net/browse/OADP-7812) | [RedHat QE] Verify Bug  OADP-3378 - Wrong/ misleading certificate error log for backup when certificate check is disabled | Aziza Karol | In Progress |
| [OADP-7813](https://redhat.atlassian.net/browse/OADP-7813) | [IBM QE-P] Verify Bug OADP-3378 - Wrong/ misleading certificate error log for backup when certificate check is disabled | Sonia Garudi | New |
| [OADP-7814](https://redhat.atlassian.net/browse/OADP-7814) | [IBM QE-Z] Verify Bug OADP-3378 - Wrong/ misleading certificate error log for backup when certificate check is disabled | Ukthi Prasad | New |

# David Vaanunu (1)

## Bugs (1)

### [OADP-4855](https://redhat.atlassian.net/browse/OADP-4855) — Kopia leaving cache on worker node
**Priority:** Blocker | **Status:** ON_QA

_No subtasks found._

# Md Nadeem (1)

## Bugs (1)

### [OADP-7132](https://redhat.atlassian.net/browse/OADP-7132) — openshift-velero-plugin panics with 'concurrent map writes'
**Priority:** Undefined | **Status:** ON_QA

_No subtasks found._

# Prasad Joshi (3)

## Bugs (3)

### [OADP-4743](https://redhat.atlassian.net/browse/OADP-4743) — DataMover restore partially fails when node selector spec is used
**Priority:** Critical | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7796](https://redhat.atlassian.net/browse/OADP-7796) | [RedHat QE] Verify Bug  OADP-4743 - DataMover restore partially fails when node selector spec is used | Prasad Joshi | Closed |
| [OADP-7797](https://redhat.atlassian.net/browse/OADP-7797) | [IBM QE-P] Verify Bug OADP-4743 - DataMover restore partially fails when node selector spec is used | Sonia Garudi | Closed |
| [OADP-7798](https://redhat.atlassian.net/browse/OADP-7798) | [IBM QE-Z] Verify Bug OADP-4743 - DataMover restore partially fails when node selector spec is used | Ukthi Prasad | New |

### [OADP-6764](https://redhat.atlassian.net/browse/OADP-6764) — Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path
**Priority:** Critical | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7803](https://redhat.atlassian.net/browse/OADP-7803) | [RedHat QE] Verify Bug  OADP-6764 - Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path | Prasad Joshi | Closed |
| [OADP-7804](https://redhat.atlassian.net/browse/OADP-7804) | [IBM QE-P] Verify Bug OADP-6764 - Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path | Sonia Garudi | New |
| [OADP-7805](https://redhat.atlassian.net/browse/OADP-7805) | [IBM QE-Z] Verify Bug OADP-6764 - Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path | Ukthi Prasad | New |

### [OADP-7381](https://redhat.atlassian.net/browse/OADP-7381) — [CSI] VGS restore fails when used with Ceph RBD storage class 
**Priority:** Critical | **Status:** ON_QA

_No subtasks found._

# Pratik Mane (3)

## Bugs (3)

### [OADP-3039](https://redhat.atlassian.net/browse/OADP-3039) — PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7815](https://redhat.atlassian.net/browse/OADP-7815) | [RedHat QE] Verify Bug  OADP-3039 - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Prasad Joshi | Closed |
| [OADP-7816](https://redhat.atlassian.net/browse/OADP-7816) | [IBM QE-P] Verify Bug OADP-3039 - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Sonia Garudi | New |
| [OADP-7817](https://redhat.atlassian.net/browse/OADP-7817) | [IBM QE-Z] Verify Bug OADP-3039 - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Ukthi Prasad | New |

### [OADP-3759](https://redhat.atlassian.net/browse/OADP-3759) — Velero shouldn't restore the restore-wait init container
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7809](https://redhat.atlassian.net/browse/OADP-7809) | [RedHat QE] Verify Bug  OADP-3759 - Velero shouldn't restore the restore-wait init container | Prasad Joshi | Closed |
| [OADP-7810](https://redhat.atlassian.net/browse/OADP-7810) | [IBM QE-P] Verify Bug OADP-3759 - Velero shouldn't restore the restore-wait init container | Sonia Garudi | New |
| [OADP-7811](https://redhat.atlassian.net/browse/OADP-7811) | [IBM QE-Z] Verify Bug OADP-3759 - Velero shouldn't restore the restore-wait init container | Ukthi Prasad | New |

### [OADP-3360](https://redhat.atlassian.net/browse/OADP-3360) — PVC has a left out label related to volumeSnapshot after success FileSystem Restore
**Priority:** Minor | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7821](https://redhat.atlassian.net/browse/OADP-7821) | [RedHat QE] Verify Bug  OADP-3360 - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Prasad Joshi | Closed |
| [OADP-7822](https://redhat.atlassian.net/browse/OADP-7822) | [IBM QE-P] Verify Bug OADP-3360 - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Sonia Garudi | New |
| [OADP-7823](https://redhat.atlassian.net/browse/OADP-7823) | [IBM QE-Z] Verify Bug OADP-3360 - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Ukthi Prasad | New |

# Tareq Alayan (1)

## Bugs (1)

### [OADP-5777](https://redhat.atlassian.net/browse/OADP-5777) — Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec.
**Priority:** Undefined | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7825](https://redhat.atlassian.net/browse/OADP-7825) | [RedHat QE] Verify Bug  OADP-5777 - Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Prasad Joshi | New |
| [OADP-7826](https://redhat.atlassian.net/browse/OADP-7826) | [IBM QE-P] Verify Bug OADP-5777 - Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Sonia Garudi | New |
| [OADP-7827](https://redhat.atlassian.net/browse/OADP-7827) | [IBM QE-Z] Verify Bug OADP-5777 - Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Ukthi Prasad | New |

# Wesley Hayutin (2)

## Bugs (2)

### [OADP-6880](https://redhat.atlassian.net/browse/OADP-6880) — VolumeGroupSnapshots doesn't respect volumePolicies
**Priority:** Major | **Status:** ON_QA

_No subtasks found._

### [OADP-3692](https://redhat.atlassian.net/browse/OADP-3692) — Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec
**Priority:** Minor | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7818](https://redhat.atlassian.net/browse/OADP-7818) | [RedHat QE] Verify Bug  OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Prasad Joshi | New |
| [OADP-7819](https://redhat.atlassian.net/browse/OADP-7819) | [IBM QE-P] Verify Bug OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Sonia Garudi | New |
| [OADP-7820](https://redhat.atlassian.net/browse/OADP-7820) | [IBM QE-Z] Verify Bug OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Ukthi Prasad | New |
