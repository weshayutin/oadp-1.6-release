# OADP 1.6.0 QE Report (ON_QA, Testing)

**JQL:** `project = OADP AND fixVersion = "OADP 1.6.0" AND issuetype in (Bug, Task, Epic, Story) AND status in ("ON_QA", "Testing") ORDER BY priority DESC, created DESC`

**Total issues:** 52  
**QA Contacts:** 7  
**Generated:** 2026-04-27

---

## Summary

| QA Contact | Bugs (11) | Tasks (2) | Storys (39) | Total |
|----------|-------|-------|-------|-------|
| Aziza Karol | [2](#aziza-karol) | — | [11](#aziza-karol) | **13** |
| David Vaanunu | [1](#david-vaanunu) | — | [1](#david-vaanunu) | **2** |
| No QA Contact | — | [1](#no-qa-contact) | [27](#no-qa-contact) | **28** |
| Prasad Joshi | [3](#prasad-joshi) | [1](#prasad-joshi) | — | **4** |
| Pratik Mane | [3](#pratik-mane) | — | — | **3** |
| Tareq Alayan | [1](#tareq-alayan) | — | — | **1** |
| Wesley Hayutin | [1](#wesley-hayutin) | — | — | **1** |
| **Total** | **11** | **2** | **39** | **52** |

---

# Aziza Karol (13)

## Bugs (2)

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

## Storys (11)

### [OADP-3971](https://redhat.atlassian.net/browse/OADP-3971) — Additional secrets cannot be added to velero pod without restart
**Priority:** Critical | **Status:** Testing

_No subtasks found._

### [OADP-7513](https://redhat.atlassian.net/browse/OADP-7513) — Backup and Restore Custom SCC Associated with ClusterRole/ClusterRoleBinding
**Priority:** Critical | **Status:** Testing

_No subtasks found._

### [OADP-2785](https://redhat.atlassian.net/browse/OADP-2785) — Add possibility to configure "priorityClassName" for node-agent daemonset through DPA
**Priority:** Major | **Status:** Testing

_No subtasks found._

### [OADP-6688](https://redhat.atlassian.net/browse/OADP-6688) — Velero scheduled backups accumulate in New state queue during extended blocking scenarios
**Priority:** Major | **Status:** Testing

_No subtasks found._

### [OADP-6694](https://redhat.atlassian.net/browse/OADP-6694) — Repository maintenance jobs do not inherit tolerations from Velero deployment
**Priority:** Major | **Status:** Testing

_No subtasks found._

### [OADP-6176](https://redhat.atlassian.net/browse/OADP-6176) — Support wildcards for namespace backup
**Priority:** Normal | **Status:** Testing

_No subtasks found._

### [OADP-6578](https://redhat.atlassian.net/browse/OADP-6578) — CLI internationalization and localization support
**Priority:** Undefined | **Status:** Testing

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

### [OADP-6724](https://redhat.atlassian.net/browse/OADP-6724) — Repo cache volume -- DU deliver snapshot size to DD
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6726](https://redhat.atlassian.net/browse/OADP-6726) — Check whether it's possible to remove VolumeSnapshotClass from the CSI B/R
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6739](https://redhat.atlassian.net/browse/OADP-6739) — VolumePolicy support for Phase condition of PVC to allow skipping Pending PVCs
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

# David Vaanunu (2)

## Bugs (1)

### [OADP-4855](https://redhat.atlassian.net/browse/OADP-4855) — Kopia leaving cache on worker node
**Priority:** Blocker | **Status:** ON_QA

_No subtasks found._

## Storys (1)

### [OADP-6693](https://redhat.atlassian.net/browse/OADP-6693) — Address sparsify requirement post DM restore on ODF.
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

# No QA Contact (28)

## Tasks (1)

### [OADP-7483](https://redhat.atlassian.net/browse/OADP-7483) — [DOC] Issue with OADP docs navigation
**Priority:** Major | **Status:** Testing

_No subtasks found._

## Storys (27)

### [OADP-6360](https://redhat.atlassian.net/browse/OADP-6360) — Add support for adding annotations to PodConfig
**Priority:** Major | **Status:** Testing

_No subtasks found._

### [OADP-6547](https://redhat.atlassian.net/browse/OADP-6547) — Include must-gather in the oadp-cli
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6555](https://redhat.atlassian.net/browse/OADP-6555) — oc oadp is defaulting to openshift-oadp namespace
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6564](https://redhat.atlassian.net/browse/OADP-6564) — CLI configuration file management
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6565](https://redhat.atlassian.net/browse/OADP-6565) — Support for multiple cluster contexts
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6566](https://redhat.atlassian.net/browse/OADP-6566) — Restore operation validation and dry-run
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6567](https://redhat.atlassian.net/browse/OADP-6567) — CLI output formatting options (JSON, YAML, table)
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6570](https://redhat.atlassian.net/browse/OADP-6570) — Cross-cluster backup and restore operations
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6571](https://redhat.atlassian.net/browse/OADP-6571) — CLI plugin auto-update mechanism
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6575](https://redhat.atlassian.net/browse/OADP-6575) — Backup encryption configuration through CLI
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6582](https://redhat.atlassian.net/browse/OADP-6582) — Implement VolumeGroupSnapshot (VGS) support in Velero
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6720](https://redhat.atlassian.net/browse/OADP-6720) — Repo cache volume -- cache volume for pod volume restore
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6721](https://redhat.atlassian.net/browse/OADP-6721) — Repo cache volume -- cache volume for data mover restore
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6722](https://redhat.atlassian.net/browse/OADP-6722) — Repo cache volume -- Unified Repo support cache volume configuration
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6723](https://redhat.atlassian.net/browse/OADP-6723) — Repo cache volume -- PVB deliver snapshot size to PVR
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6729](https://redhat.atlassian.net/browse/OADP-6729) — Deprecate Changing PVC selected-node feature
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6731](https://redhat.atlassian.net/browse/OADP-6731) — Data mover expose diagnostic -- add events to diagnostic
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6732](https://redhat.atlassian.net/browse/OADP-6732) — configMap validation in CLI should print the error when fails
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6733](https://redhat.atlassian.net/browse/OADP-6733) — Maintenance Metrics
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6734](https://redhat.atlassian.net/browse/OADP-6734) — maintenance jobs labels required for network-policies
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6735](https://redhat.atlassian.net/browse/OADP-6735) — Behavioral change to default datamover behavior in go 1.25
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6736](https://redhat.atlassian.net/browse/OADP-6736) — Backup Repository controller may OOM kill Velero server when checking repo existence
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-6737](https://redhat.atlassian.net/browse/OADP-6737) — Concurrent backup processing
**Priority:** Undefined | **Status:** Testing

_No subtasks found._

### [OADP-7455](https://redhat.atlassian.net/browse/OADP-7455) — (QE) Add test Coverage for Velero 1.18 features
**Priority:** Undefined | **Status:** Testing

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7468](https://redhat.atlassian.net/browse/OADP-7468) | (QE) Repository Cache Volume Feature- Test Coverage | Md Nadeem | New |
| [OADP-7469](https://redhat.atlassian.net/browse/OADP-7469) | (QE) Wildcard Namespace Support- Test Coverage | Prasad Joshi | In Progress |
| [OADP-7472](https://redhat.atlassian.net/browse/OADP-7472) | (QE) GenerateName Resource Handling- Test Coverage | Tareq Alayan | New |
| [OADP-7473](https://redhat.atlassian.net/browse/OADP-7473) | (QE) RBAC Restore Ordering- Test Coverage | Tareq Alayan | New |
| [OADP-7474](https://redhat.atlassian.net/browse/OADP-7474) |  (QE) Privileged FS Backup Pods- Test Coverage | Aziza Karol | New |
| [OADP-7475](https://redhat.atlassian.net/browse/OADP-7475) | (QE) VolumePolicy VolumeGroupSnapshot- Test Coverage | Prasad Joshi | In Progress |
| [OADP-7828](https://redhat.atlassian.net/browse/OADP-7828) | (QE) Incremental size for data movers | Prasad Joshi | In Progress |

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

# Prasad Joshi (4)

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

# Wesley Hayutin (1)

## Bugs (1)

### [OADP-3692](https://redhat.atlassian.net/browse/OADP-3692) — Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec
**Priority:** Minor | **Status:** ON_QA

**Platform Validation Tasks:**

| Task | Summary | Assignee | Status |
|------|---------|----------|--------|
| [OADP-7818](https://redhat.atlassian.net/browse/OADP-7818) | [RedHat QE] Verify Bug  OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Wesley Hayutin | Release Pending |
| [OADP-7819](https://redhat.atlassian.net/browse/OADP-7819) | [IBM QE-P] Verify Bug OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Sonia Garudi | Closed |
| [OADP-7820](https://redhat.atlassian.net/browse/OADP-7820) | [IBM QE-Z] Verify Bug OADP-3692 - Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | Ukthi Prasad | New |
