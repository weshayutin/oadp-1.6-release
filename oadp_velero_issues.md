# OADP Issues and Upstream Velero Issue Mapping

This document contains a mapping of OADP Jira issues to their associated upstream Velero GitHub issues and labels.

**Query Used:** `project = OADP AND status not in (Closed) AND (fixVersion = "OADP 1.6.0" OR fixVersion = "OADP 1.6.0") AND (labels = oadp_upstream_bug_fix ) ORDER BY priority DESC, Rank ASC`

## Jira to Upstream Candidate

*Note: OADP issues that reference Velero v1.18 milestone issues are shown in the milestone cross-reference section below.*

| Jira Issue | Upstream Velero Issue(s) | Upstream Velero Issue Labels |
|------------|---------------------------|------------------------------|
| [OADP-3971](https://issues.redhat.com/browse/OADP-3971) - Additional secrets cannot be added to velero pod without restart | [#8692](https://github.com/vmware-tanzu/velero/issues/8692) - aws plugin: CustomerKeyEncryptionFile can be read in from secret rather than path on velero pod. (closed)<br>[#7767](https://github.com/vmware-tanzu/velero/issues/7767) - Ability to add additional files from secret(s) to Velero pod without restart (closed) | **#8692**: Area/Cloud/AWS, backlog, Reviewed Q2 2025<br>**#7767**: *No labels* |
| [OADP-4743](https://issues.redhat.com/browse/OADP-4743) - DataMover restore partially fails when node selector spec is used | [#8242](https://github.com/vmware-tanzu/velero/issues/8242) - DataMover - distribute datadownload evenly across nodes if possible (closed)<br>[#8186](https://github.com/vmware-tanzu/velero/issues/8186) - Restore Data Movement Node Selection  (closed) | **#8242**: backlog, area/datamover, Reviewed Q3 2024<br>**#8186**: kind/requirement, backlog, area/datamover, Reviewed Q2 2025 |
| [OADP-5645](https://issues.redhat.com/browse/OADP-5645) - OADP CSI Snapshot shows successful, but size is 0 bytes | [#6506](https://github.com/vmware-tanzu/velero/issues/6506) - How can I get the size of the backups and snapshots ? (open) | **#6506**: kind/requirement, Needs triage, depends-upstream, backlog, Reviewed Q2 2025, 1.18-candidate, Reviewed Q3 2025 |
| [OADP-5739](https://issues.redhat.com/browse/OADP-5739) - XFS/Ext4 PVC restore fails if volume usage is 100% | [#2812](https://github.com/vmware-tanzu/velero/issues/2812) - Restore fails with error "no space left on device" if PVCs are 100% utilised during backup (open) | **#2812**: kind/Bug, Restic - GA, Reviewed Q2 2021, Needs triage, area/fs-backup, 1.18-candidate, Reviewed Q3 2025 |
| [OADP-4855](https://issues.redhat.com/browse/OADP-4855) - Kopia leaving cache on worker node | [#7725](https://github.com/vmware-tanzu/velero/issues/7725) - Make kopia repo cache place configurable (open)<br>[#8443](https://github.com/vmware-tanzu/velero/issues/8443) - Mechanism to run maintenance of Kopia's cache directory within the node-agent (closed) | **#7725**: Performance, backlog, Needs Design, repository, scalability, Reviewed Q2 2025, 1.18-candidate<br>**#8443**: Needs info, Needs triage, 1.16-candidate |
| [OADP-6599](https://issues.redhat.com/browse/OADP-6599) - [Chaos][OADP] OADP backup VM PartiallyFailed when draining VM host node during backup | *No upstream GitHub issue found* | *N/A* |
| [OADP-2938](https://issues.redhat.com/browse/OADP-2938) - Backup should immediately fail when nodeAgent pods are not running | *No upstream GitHub issue found* | *N/A* |
| [OADP-3039](https://issues.redhat.com/browse/OADP-3039) - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | [#8809](https://github.com/vmware-tanzu/velero/issues/8809) - VGDP Micro Service for fs-backup (closed)<br>[#8961](https://github.com/vmware-tanzu/velero/issues/8961) - VGDP ms for fs-backup - cancel PVB/PVR on Velero server restart (closed) | **#8809**: Area/WindowsSupport, area/fs-backup, scalability, Area/NFS-Support<br>**#8961**: area/fs-backup |
| [OADP-3759](https://issues.redhat.com/browse/OADP-3759) - Velero shouldn't restore the restore-wait init container | [#8870](https://github.com/vmware-tanzu/velero/issues/8870) - Velero shouldn't restore the restore-wait init container (closed)<br>[#3519](https://github.com/vmware-tanzu/velero/issues/3519) - Allow not skipping Complete jobs in velero restores. (open) | **#8870**: area/fs-backup, Reviewed Q2 2025<br>**#3519**: Needs triage, backlog, Needs Design, Reviewed Q2 2025, 1.18-candidate, Reviewed Q3 2025 |
| [OADP-4289](https://issues.redhat.com/browse/OADP-4289) - Velero fails to patch managed fields on namespace resources which causing restore to partially fail | [#8132](https://github.com/vmware-tanzu/velero/issues/8132) - Random race condition in the restore with managed fields (open) | **#8132**: kind/Bug, Needs triage, 1.18-candidate |
| [OADP-4572](https://issues.redhat.com/browse/OADP-4572) - Namespace label selector not working for backups as expected | [#7697](https://github.com/vmware-tanzu/velero/pull/7697) - Modify namespace filter logic for backup with label selector (closed)<br>[#8342](https://github.com/vmware-tanzu/velero/pull/8342) - Namespaces included by labelSelector act as IncludedNamespaces for Backup (open) | **#7697**: has-unit-tests, has-changelog, target/FC<br>**#8342**: has-unit-tests, Documentation, has-changelog |
| [OADP-5114](https://issues.redhat.com/browse/OADP-5114) - Incompatibility of OADP with data mover restore | [#8186](https://github.com/vmware-tanzu/velero/issues/8186) - Restore Data Movement Node Selection  (closed) | **#8186**: kind/requirement, backlog, area/datamover, Reviewed Q2 2025 |
| [OADP-5516](https://issues.redhat.com/browse/OADP-5516) - Support to have Singed backups and local checksums for backup integrity | [#9187](https://github.com/vmware-tanzu/velero/issues/9187) - Implement Backup Integrity Verification for Data Corruption Detection (open)<br>[#1072](https://github.com/vmware-tanzu/velero/issues/1072) - Backup checksums (open)<br>[#3875](https://github.com/vmware-tanzu/velero/issues/3875) - Support for data integrity and data trust of the backups (open) | **#9187**: Needs triage, 1.18-candidate, Reviewed Q3 2025<br>**#1072**: Enhancement/User, Reviewed Q2 2021, Icebox, kind/requirement<br>**#3875**: Enhancement/User, Needs Product, kind/requirement |
| [OADP-3360](https://issues.redhat.com/browse/OADP-3360) - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | [#8894](https://github.com/vmware-tanzu/velero/issues/8894) - PVC has a left out label related to volumeSnapshot after success FileSystem Restore (open) | **#8894**: Needs triage, env/openshift, 1.18-candidate |
| [OADP-5171](https://issues.redhat.com/browse/OADP-5171) - BSL status.message field shouldn't have the http response as output when bucket doesn't exist | [#8368](https://github.com/vmware-tanzu/velero/issues/8368) - BSL status.message field shouldn't have the http response as output when bucket doesn't exist (open) | **#8368**: Help wanted, Area/Cloud/Azure, Good first issue, Reviewed Q2 2025, 1.18-candidate |
| [OADP-5829](https://issues.redhat.com/browse/OADP-5829) - wrong S3 identifier (resticIdentifier) while using a kopia BackupRepository  | [#8830](https://github.com/vmware-tanzu/velero/issues/8830) - Invalid path in BackupRepository (closed) | **#8830**: Restic, backlog, restic-deprecate, repository, Reviewed Q2 2025 |
| [OADP-6525](https://issues.redhat.com/browse/OADP-6525) - Dramatic performance dropoff over time - Velero backup performance degradation | [#9169](https://github.com/vmware-tanzu/velero/issues/9169) - Dramatic performance dropoff over time (open) | **#9169**: Performance, Needs info, Needs investigation, 1.18-candidate |

## Summary

- **Total Issues**: 18
- **Issues in Candidate Table**: 17
- **Issues Referenced in Milestone Section**: 1
- **Issues with Upstream GitHub Issues**: 15
- **Issues without Upstream GitHub Issues**: 2

## Velero v1.18 Milestone Issues Cross-Reference

This section lists all issues in the [Velero v1.18 milestone](https://github.com/vmware-tanzu/velero/issues?q=is%3Aissue%20milestone%3Av1.18) and identifies which ones are also referenced by OADP issues above.

| Velero Issue | Status | Labels | Associated OADP Issue(s) |
|--------------|--------|--------|-------------------------|
| [#7904](https://github.com/vmware-tanzu/velero/issues/7904) - Deprecate Changing PVC selected-node feature (open) | Open | Breaking change, doc-change-required, feature-deprecation | *Not referenced by OADP issues* |
| [#1874](https://github.com/vmware-tanzu/velero/issues/1874) - Wildcards don't work for namespaces (open) | Open | kind/Bug, Needs investigation, Reviewed Q2 2021, 2024 Q2 reviewed, Reviewed Q3 2025 | [OADP-6176](https://issues.redhat.com/browse/OADP-6176) |

### Velero v1.18 Milestone Summary

- **Total Velero v1.18 Issues**: 2
- **Issues Referenced by OADP**: 1
- **Issues Not Referenced by OADP**: 1
