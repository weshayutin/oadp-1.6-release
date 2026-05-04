# OADP 1.6.0 QE Report (ON_QA, Testing)

**JQL:** `project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic, Story) AND status in ("ON_QA", "Testing") AND component != "Documentation" ORDER BY priority DESC, created DESC`

**Total issues:** 18  
**QA Contacts:** 7  
**Generated:** 2026-05-04

---

## Summary

| QA Contact | Bugs (9) | Tasks (1) | Storys (8) | Total |
|----------|-------|-------|-------|-------|
| Aziza Karol | [1](#aziza-karol) | — | [3](#aziza-karol) | **4** |
| David Vaanunu | — | — | [1](#david-vaanunu) | **1** |
| No QA Contact | — | — | [4](#no-qa-contact) | **4** |
| Prasad Joshi | [2](#prasad-joshi) | [1](#prasad-joshi) | — | **3** |
| Pratik Mane | [3](#pratik-mane) | — | — | **3** |
| Tareq Alayan | [2](#tareq-alayan) | — | — | **2** |
| Wesley Hayutin | [1](#wesley-hayutin) | — | — | **1** |
| **Total** | **9** | **1** | **8** | **18** |

---

# Aziza Karol (4)

## Bugs (1)

### [OADP-3378](https://redhat.atlassian.net/browse/OADP-3378) — Wrong/ misleading certificate error log for backup when certificate check is disabled
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7812](https://redhat.atlassian.net/browse/OADP-7812) | [RedHat QE] Verify Bug  OADP-3378 - Wrong/ misleading certificate error log for backup when certificate check is disabled | Aziza Karol | In Progress |
| [OADP-7813](https://redhat.atlassian.net/browse/OADP-7813) | [IBM QE-P] Verify Bug OADP-3378 - Wrong/ misleading certificate error log for backup when certificate check is disabled | Sonia Garudi | New |
| [OADP-7814](https://redhat.atlassian.net/browse/OADP-7814) | [IBM QE-Z] Verify Bug OADP-3378 - Wrong/ misleading certificate error log for backup when certificate check is disabled | Ukthi Prasad | New |

## Storys (3)

### [OADP-3971](https://redhat.atlassian.net/browse/OADP-3971) — Additional secrets cannot be added to velero pod without restart
**Priority:** Critical | **Status:** Testing

_No subtasks found._

### [OADP-2785](https://redhat.atlassian.net/browse/OADP-2785) — Add possibility to configure "priorityClassName" for node-agent daemonset through DPA
**Priority:** Major | **Status:** Testing

_No subtasks found._

### [OADP-6712](https://redhat.atlassian.net/browse/OADP-6712) — (Dev) ( VolumeGroupSnapshot Support Implementation ) implementation
**Priority:** Undefined | **Status:** Testing

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-6713](https://redhat.atlassian.net/browse/OADP-6713) | (Dev) [smoke automation tests]  VolumeGroupSnapshot Support Implementation | Wesley Hayutin | Closed |
| [OADP-6714](https://redhat.atlassian.net/browse/OADP-6714) | (QE)[Manual testing for]  VolumeGroupSnapshot Support Implementation | Prasad Joshi | In Progress |
| [OADP-6715](https://redhat.atlassian.net/browse/OADP-6715) | (QE)[Complete automation for]  VolumeGroupSnapshot Support Implementation | Prasad Joshi | In Progress |
| [OADP-6716](https://redhat.atlassian.net/browse/OADP-6716) | (QE)[Test plan internal review for]  VolumeGroupSnapshot Support Implementation | Aziza Karol | New |
| [OADP-6718](https://redhat.atlassian.net/browse/OADP-6718) | [Test plan review for]  VolumeGroupSnapshot Support Implementation | Wesley Hayutin | New |

# David Vaanunu (1)

## Storys (1)

### [OADP-6693](https://redhat.atlassian.net/browse/OADP-6693) — Address sparsify requirement post DM restore on ODF.
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

# No QA Contact (4)

## Storys (4)

### [OADP-6360](https://redhat.atlassian.net/browse/OADP-6360) — Add support for adding annotations to PodConfig
**Priority:** Major | **Status:** Testing

_No subtasks found._

### [OADP-7662](https://redhat.atlassian.net/browse/OADP-7662) — [JIRA-AUTO-TEST] OADP 1.6.0 Test Matrix Run
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-7663](https://redhat.atlassian.net/browse/OADP-7663) — (QE) (jira-auto) Automation Failure & skipped Analysis 1.6.0-202603271629 and Update RP
**Priority:** Undefined | **Status:** Testing

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7664](https://redhat.atlassian.net/browse/OADP-7664) | (QE) (jira-auto) KUBEVIRT_GCP_GCP | Unassigned | New |
| [OADP-7666](https://redhat.atlassian.net/browse/OADP-7666) | (QE) (jira-auto) AWS_AWSS3 | Unassigned | New |
| [OADP-7670](https://redhat.atlassian.net/browse/OADP-7670) | (QE) (jira-auto) AWS_SNO | Unassigned | New |
| [OADP-7671](https://redhat.atlassian.net/browse/OADP-7671) | (QE) (jira-auto) GCP_GCP | Unassigned | Closed |
| [OADP-7672](https://redhat.atlassian.net/browse/OADP-7672) | (QE) (jira-auto) GCP_GCP | Pratik Mane | Closed |
| [OADP-7675](https://redhat.atlassian.net/browse/OADP-7675) | (QE) (jira-auto) GCP_GCP | Unassigned | Closed |
| [OADP-7676](https://redhat.atlassian.net/browse/OADP-7676) | (QE) (jira-auto) GCP_GCP | Unassigned | Closed |

### [OADP-7835](https://redhat.atlassian.net/browse/OADP-7835) — (QE) (jira-auto) Automation Failure & skipped Analysis 1.6.0-202604161726 and Update RP
**Priority:** Undefined | **Status:** Testing

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7836](https://redhat.atlassian.net/browse/OADP-7836) | (QE) (jira-auto) BACKUPLIB-RESTORE | Unassigned | In Progress |
| [OADP-7838](https://redhat.atlassian.net/browse/OADP-7838) | (QE) (jira-auto) KUBEVIRT_GCP_GCP | Pratik Mane | Closed |
| [OADP-7839](https://redhat.atlassian.net/browse/OADP-7839) | (QE) (jira-auto) AZURE_SELF_SERVICE | Prasad Joshi | Closed |
| [OADP-7840](https://redhat.atlassian.net/browse/OADP-7840) | (QE) (jira-auto) AWS_SELF_SERVICE | Prasad Joshi | Closed |
| [OADP-7841](https://redhat.atlassian.net/browse/OADP-7841) | (QE) (jira-auto) GCP_SELF_SERVICE | Prasad Joshi | Closed |
| [OADP-7842](https://redhat.atlassian.net/browse/OADP-7842) | (QE) (jira-auto) GCP_GCP | Prasad Joshi | Closed |
| [OADP-7843](https://redhat.atlassian.net/browse/OADP-7843) | (QE) (jira-auto) CEPHFS_AWS_AWSS3 | Prasad Joshi | Closed |
| [OADP-7844](https://redhat.atlassian.net/browse/OADP-7844) | (QE) (jira-auto) AWS_AWSS3 | Prasad Joshi | Closed |
| [OADP-7845](https://redhat.atlassian.net/browse/OADP-7845) | (QE) (jira-auto) GCP_GCPS3 | Prasad Joshi | Closed |
| [OADP-7846](https://redhat.atlassian.net/browse/OADP-7846) | (QE) (jira-auto) AWSPROXY_AWSS3 | Prasad Joshi | Closed |
| [OADP-7847](https://redhat.atlassian.net/browse/OADP-7847) | (QE) (jira-auto) AZURE_AZURE | Pratik Mane | Closed |
| [OADP-7848](https://redhat.atlassian.net/browse/OADP-7848) | (QE) (jira-auto) AZURE_AZURE_SAK | Prasad Joshi | Closed |
| [OADP-7849](https://redhat.atlassian.net/browse/OADP-7849) | (QE) (jira-auto) AWS_MCG | Prasad Joshi | Closed |
| [OADP-7850](https://redhat.atlassian.net/browse/OADP-7850) | (QE) (jira-auto) AWS_SNO | Prasad Joshi | Closed |

# Prasad Joshi (3)

## Bugs (2)

### [OADP-4855](https://redhat.atlassian.net/browse/OADP-4855) — Kopia leaving cache on worker node
**Priority:** Blocker | **Status:** ON_QA

_No subtasks found._

### [OADP-7381](https://redhat.atlassian.net/browse/OADP-7381) — [CSI] VGS restore fails when used with Ceph RBD storage class 
**Priority:** Critical | **Status:** ON_QA

_No subtasks found._

## Tasks (1)

### [OADP-4589](https://redhat.atlassian.net/browse/OADP-4589) — Dataupload object reporting improvements
**Priority:** Major | **Status:** Testing

_No subtasks found._

# Pratik Mane (3)

## Bugs (3)

### [OADP-3039](https://redhat.atlassian.net/browse/OADP-3039) — PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7815](https://redhat.atlassian.net/browse/OADP-7815) | [RedHat QE] Verify Bug  OADP-3039 - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Prasad Joshi | Closed |
| [OADP-7816](https://redhat.atlassian.net/browse/OADP-7816) | [IBM QE-P] Verify Bug OADP-3039 - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Sonia Garudi | Closed |
| [OADP-7817](https://redhat.atlassian.net/browse/OADP-7817) | [IBM QE-Z] Verify Bug OADP-3039 - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Ukthi Prasad | Closed |

### [OADP-3759](https://redhat.atlassian.net/browse/OADP-3759) — Velero shouldn't restore the restore-wait init container
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7809](https://redhat.atlassian.net/browse/OADP-7809) | [RedHat QE] Verify Bug  OADP-3759 - Velero shouldn't restore the restore-wait init container | Prasad Joshi | Closed |
| [OADP-7810](https://redhat.atlassian.net/browse/OADP-7810) | [IBM QE-P] Verify Bug OADP-3759 - Velero shouldn't restore the restore-wait init container | Sonia Garudi | Closed |
| [OADP-7811](https://redhat.atlassian.net/browse/OADP-7811) | [IBM QE-Z] Verify Bug OADP-3759 - Velero shouldn't restore the restore-wait init container | Ukthi Prasad | New |

### [OADP-3360](https://redhat.atlassian.net/browse/OADP-3360) — PVC has a left out label related to volumeSnapshot after success FileSystem Restore
**Priority:** Minor | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7821](https://redhat.atlassian.net/browse/OADP-7821) | [RedHat QE] Verify Bug  OADP-3360 - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Prasad Joshi | Closed |
| [OADP-7822](https://redhat.atlassian.net/browse/OADP-7822) | [IBM QE-P] Verify Bug OADP-3360 - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Sonia Garudi | Closed |
| [OADP-7823](https://redhat.atlassian.net/browse/OADP-7823) | [IBM QE-Z] Verify Bug OADP-3360 - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Ukthi Prasad | Closed |

# Tareq Alayan (2)

## Bugs (2)

### [OADP-5114](https://redhat.atlassian.net/browse/OADP-5114) — Incompatibility of OADP with data mover restore
**Priority:** Normal | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7806](https://redhat.atlassian.net/browse/OADP-7806) | [RedHat QE] Verify Bug  OADP-5114 - Incompatibility of OADP with data mover restore | Tareq Alayan | Closed |
| [OADP-7807](https://redhat.atlassian.net/browse/OADP-7807) | [IBM QE-P] Verify Bug OADP-5114 - Incompatibility of OADP with data mover restore | Sonia Garudi | New |
| [OADP-7808](https://redhat.atlassian.net/browse/OADP-7808) | [IBM QE-Z] Verify Bug OADP-5114 - Incompatibility of OADP with data mover restore | Ukthi Prasad | New |

### [OADP-5777](https://redhat.atlassian.net/browse/OADP-5777) — Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec.
**Priority:** Undefined | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7825](https://redhat.atlassian.net/browse/OADP-7825) | [RedHat QE] Verify Bug  OADP-5777 - Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Tareq Alayan | In Progress |
| [OADP-7826](https://redhat.atlassian.net/browse/OADP-7826) | [IBM QE-P] Verify Bug OADP-5777 - Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Sonia Garudi | New |
| [OADP-7827](https://redhat.atlassian.net/browse/OADP-7827) | [IBM QE-Z] Verify Bug OADP-5777 - Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | Ukthi Prasad | New |

# Wesley Hayutin (1)

## Bugs (1)

### [OADP-3692](https://redhat.atlassian.net/browse/OADP-3692) — Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec
**Priority:** Minor | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7818](https://redhat.atlassian.net/browse/OADP-7818) | [RedHat QE] Verify Bug  OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Wesley Hayutin | Closed |
| [OADP-7819](https://redhat.atlassian.net/browse/OADP-7819) | [IBM QE-P] Verify Bug OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Sonia Garudi | Closed |
| [OADP-7820](https://redhat.atlassian.net/browse/OADP-7820) | [IBM QE-Z] Verify Bug OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Ukthi Prasad | New |
