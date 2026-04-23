# OADP Issues and Upstream Velero Issue Mapping

This document contains a mapping of OADP Jira issues to their associated upstream Velero GitHub issues and labels.

**Query Used:** `project = OADP AND status not in (Closed) AND (fixVersion = "OADP 1.6.0" OR fixVersion = "OADP 1.6.0") AND (labels = oadp_upstream_bug_fix ) ORDER BY priority DESC, Rank ASC`

## Jira to Upstream Candidate

*Note: OADP issues that reference Velero v1.18 milestone issues are shown in the milestone cross-reference section below.*

| Row # | Jira Issue | Jira Assignee | Upstream Velero Issue(s) | Upstream Velero Issue Labels |
|-------|------------|---------------|---------------------------|------------------------------|
| 1 | [OADP-3971](https://redhat.atlassian.net/browse/OADP-3971) - Additional secrets cannot be added to velero pod without restart | Tiger Kaovilai | ✅ **[#8692](https://github.com/velero-io/velero/issues/8692) - aws plugin: CustomerKeyEncryptionFile can be read in from secret rather than path on velero pod. (closed)**<br>✅ **[#7767](https://github.com/velero-io/velero/issues/7767) - Ability to add additional files from secret(s) to Velero pod without restart (closed)** | **#8692**: Area/Cloud/AWS, backlog, Reviewed Q2 2025<br>**#7767**: *No labels* |
| 2 | [OADP-4743](https://redhat.atlassian.net/browse/OADP-4743) - DataMover restore partially fails when node selector spec is used | Shubham Dilip Pampattiwar | ✅ **[#8242](https://github.com/velero-io/velero/issues/8242) - DataMover - distribute datadownload evenly across nodes if possible (closed)**<br>✅ **[#8186](https://github.com/velero-io/velero/issues/8186) - Restore Data Movement Node Selection  (closed)** | **#8242**: backlog, area/datamover, Reviewed Q3 2024<br>**#8186**: kind/requirement, backlog, area/datamover, Reviewed Q2 2025 |
| 5 | [OADP-2785](https://redhat.atlassian.net/browse/OADP-2785) - Add possibility to configure "priorityClassName" for node-agent daemonset through DPA | Tiger Kaovilai | ✅ **[#2010](https://github.com/velero-io/velero/issues/2010) - AWS SKD upgrade | IRSA awareness (closed)**<br>✅ **[#1224](https://github.com/velero-io/velero/issues/1224) - Get v0.11 docs site ready (closed)**<br>✅ **[#2155](https://github.com/velero-io/velero/pull/2155) - Add documentation for velero install cli (closed)** | **#2010**: *No labels*<br>**#1224**: Area/Documentation<br>**#2155**: *No labels* |
| 7 | [OADP-6688](https://redhat.atlassian.net/browse/OADP-6688) - Velero scheduled backups accumulate in New state queue during extended blocking scenarios | Shubham Dilip Pampattiwar | ✅ **[#9259](https://github.com/velero-io/velero/issues/9259) - Schedule Backup Queue Accumulation During Extended Blocking Scenarios (closed)** | **#9259**: Needs info, Area/schedule, target/v1.17.1 |
| 10 | [OADP-3039](https://redhat.atlassian.net/browse/OADP-3039) - PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | Wesley Hayutin | ✅ **[#8809](https://github.com/velero-io/velero/issues/8809) - VGDP Micro Service for fs-backup (closed)**<br>✅ **[#8961](https://github.com/velero-io/velero/issues/8961) - VGDP ms for fs-backup - cancel PVB/PVR on Velero server restart (closed)** | **#8809**: Area/WindowsSupport, area/fs-backup, scalability, Area/NFS-Support<br>**#8961**: area/fs-backup |
| 11 | [OADP-3759](https://redhat.atlassian.net/browse/OADP-3759) - Velero shouldn't restore the restore-wait init container | Tiger Kaovilai | *No upstream GitHub issue found* | *N/A* |
| 14 | [OADP-5114](https://redhat.atlassian.net/browse/OADP-5114) - Incompatibility of OADP with data mover restore | Michal Pryc | *No upstream GitHub issue found* | *N/A* |
| 18 | [OADP-5829](https://redhat.atlassian.net/browse/OADP-5829) - wrong S3 identifier (resticIdentifier) while using a kopia BackupRepository  | Tiger Kaovilai | *No upstream GitHub issue found* | *N/A* |
| 20 | [OADP-6525](https://redhat.atlassian.net/browse/OADP-6525) - Dramatic performance dropoff over time - Velero backup performance degradation | Shubham Dilip Pampattiwar | *No upstream GitHub issue found* | *N/A* |
| 22 | [OADP-6581](https://redhat.atlassian.net/browse/OADP-6581) - Tech-Preview  - VolumeGroupSnapshot Support Implementation | Shubham Dilip Pampattiwar | ✅ **[#8778](https://github.com/velero-io/velero/pull/8778) - Add design for VolumeGroupSnapshot support (closed)**<br>✅ **[#8447](https://github.com/velero-io/velero/issues/8447) - Add Support for Volume Group Snapshots in Velero (closed)** | **#8778**: Area/Design, has-changelog<br>**#8447**: Area/Design, VolumeGroupSnapshot, Needs Design |
| 23 | [OADP-6582](https://redhat.atlassian.net/browse/OADP-6582) - Implement VolumeGroupSnapshot (VGS) support in Velero | Shubham Dilip Pampattiwar | *No upstream GitHub issue found* | *N/A* |
| 26 | [OADP-6764](https://redhat.atlassian.net/browse/OADP-6764) - Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path | Scott Seago | ✅ **[#9295](https://github.com/velero-io/velero/pull/9295) - Privileged fs backup pods (closed)**<br>✅ **[#9300](https://github.com/velero-io/velero/pull/9300) - [release-1.17] Privileged fs backup pods 1.17 (closed)**<br>✅ **[#9294](https://github.com/velero-io/velero/issues/9294) - Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path (closed)** | **#9295**: has-unit-tests, Documentation, has-changelog, target/v1.17.1<br>**#9300**: Dependencies, has-unit-tests, Documentation, has-changelog<br>**#9294**: area/fs-backup, target/v1.17.1 |
| 29 | [OADP-6955](https://redhat.atlassian.net/browse/OADP-6955) - Fix the Job build error when BackupRepository name longer than 63 | Tiger Kaovilai | ✅ **[#9350](https://github.com/velero-io/velero/pull/9350) - Fix the Job build error when BackupReposiotry name longer than 63. (closed)** | **#9350**: has-unit-tests, has-changelog |
| 30 | [OADP-6923](https://redhat.atlassian.net/browse/OADP-6923) - [DOC] Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path | Andy Arnold | ✅ **[#9294](https://github.com/velero-io/velero/issues/9294) - Velero 1.17 filesystem backup is broken for clusters that require Privileged pod security context to access the mount path (closed)** | **#9294**: area/fs-backup, target/v1.17.1 |
| 31 | [OADP-6896](https://redhat.atlassian.net/browse/OADP-6896) - Node agent pod restarts cancel all DataUploads across all nodes, blocking backup queue in OADP 1.5 | Tiger Kaovilai | ✅ **[#8534](https://github.com/velero-io/velero/issues/8534) - Only DU/DD accepted by the restarted node should be cancelled (closed)**<br>✅ **[#8952](https://github.com/velero-io/velero/pull/8952) - DM controller refactor for cancel (closed)** | **#8534**: backlog, area/datamover, downstream-integration, robustness<br>**#8952**: has-unit-tests, has-changelog |
| 32 | [OADP-6911](https://redhat.atlassian.net/browse/OADP-6911) - [Upstream] Restore CR Completed while PodVolumeRestore CR is InProgress | Wesley Hayutin | *No upstream GitHub issue found* | *N/A* |
| 33 | [OADP-4855](https://redhat.atlassian.net/browse/OADP-4855) - Kopia leaving cache on worker node | Michal Pryc | ✅ **[#2090](https://github.com/velero-io/velero/issues/2090) - allow for kustomize customizations before objects are restored (closed)**<br>✅ **[#8443](https://github.com/velero-io/velero/issues/8443) - Mechanism to run maintenance of Kopia's cache directory within the node-agent (closed)**<br>✅ **[#7725](https://github.com/velero-io/velero/issues/7725) - Make kopia repo cache place configurable (closed)** | **#2090**: Enhancement/User, Reviewed Q2 2021<br>**#8443**: Needs info, Needs triage, 1.16-candidate<br>**#7725**: Performance, backlog, Needs Design, repository, downstream-integration, scalability, Reviewed Q2 2025 |
| 34 | [OADP-6579](https://redhat.atlassian.net/browse/OADP-6579) - Concurrent Backup Processing Implementation | Scott Seago | ✅ **[#8991](https://github.com/velero-io/velero/pull/8991) - Concurrent backup design doc (closed)**<br>✅ **[#9243](https://github.com/velero-io/velero/issues/9243) - Concurrent backup processing (closed)**<br>✅ **[#8899](https://github.com/velero-io/velero/issues/8899) - Design for running multiple backups in parallel (closed)** | **#8991**: Area/Design, kind/changelog-not-required<br>**#9243**: Reviewed Q3 2025<br>**#8899**: *No labels* |
| 35 | [OADP-6694](https://redhat.atlassian.net/browse/OADP-6694) - Repository maintenance jobs do not inherit tolerations from Velero deployment | Shubham Dilip Pampattiwar | ✅ **[#9256](https://github.com/velero-io/velero/pull/9256) - Fix maintenance jobs toleration inheritance from Velero deployment (closed)**<br>✅ **[#9245](https://github.com/velero-io/velero/issues/9245) - Repository maintenance jobs do not inherit tolerations from Velero deployment (closed)** | **#9256**: has-unit-tests, has-changelog<br>**#9245**: backup-repo/Maintenance, target/v1.17.1 |
| 36 | [OADP-6880](https://redhat.atlassian.net/browse/OADP-6880) - VolumeGroupSnapshots doesn't respect volumePolicies | Shubham Dilip Pampattiwar | ✅ **[#9344](https://github.com/velero-io/velero/issues/9344) - VolumeGroupSnaphosts don't respect VolumePolicies (closed)** | **#9344**: VolumeGroupSnapshot |
| 37 | [OADP-6176](https://redhat.atlassian.net/browse/OADP-6176) - Support wildcards for namespace backup | Joseph Antony Vaikath | *No upstream GitHub issue found* | *N/A* |
| 38 | [OADP-6879](https://redhat.atlassian.net/browse/OADP-6879) - Volume policy is in low performance when there are lots of pods and PVCs in the cluster | Shubham Dilip Pampattiwar | *No upstream GitHub issue found* | *N/A* |
| 39 | [OADP-3360](https://redhat.atlassian.net/browse/OADP-3360) - PVC has a left out label related to volumeSnapshot after success FileSystem Restore | Joseph Antony Vaikath | *No upstream GitHub issue found* | *N/A* |
| 40 | [OADP-5171](https://redhat.atlassian.net/browse/OADP-5171) - BSL status.message field shouldn't have the http response as output when bucket doesn't exist | Shubham Dilip Pampattiwar | *No upstream GitHub issue found* | *N/A* |

## Summary

- **Total Issues**: 24
- **Issues in Candidate Table**: 24
- **Issues Referenced in Milestone Section**: 0
- **Issues with Upstream GitHub Issues**: 14
- **Issues without Upstream GitHub Issues**: 10

## Velero v1.18 Milestone Issues Cross-Reference

This section lists all issues in the [Velero v1.18 milestone](https://github.com/vmware-tanzu/velero/issues?q=is%3Aissue%20milestone%3Av1.18) and identifies which ones are also referenced by OADP issues above.

| Row # | Velero Issue | Status | Labels | Associated OADP Issue(s) | Jira Assignee |
|-------|--------------|--------|--------|-------------------------|---------------|

### Velero v1.18 Milestone Summary

- **Total Velero v1.18 Issues**: 0
- **Issues Referenced by OADP**: 0
- **Issues Not Referenced by OADP**: 0
