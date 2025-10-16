# OADP 1.6.0 Jira summary

## tkaovila@redhat.com

| Issue Number | Description | Status | Priority | Date Updated |
|--------------|-------------|--------|----------|--------------|
| OADP-6739 | VolumePolicy support for Phase condition of PVC to allow skipping Pending PVCs | New | Undefined | 2025-10-16 17:14:48 |
| OADP-6738 | Select namespace to include by its labelSelector | New | Undefined | 2025-10-16 17:10:31 |
| OADP-5831 | Do not restore failed or currently running jobs | New | Normal | 2025-10-16 16:28:54 |
| OADP-5777 | Backup Partially Fails with AWS bucket with " region not found ", in absence of VSL spec. | New | Undefined | 2025-08-08 21:10:33 |
| OADP-5739 | XFS/Ext4 PVC restore fails if volume usage is 100% | New | Critical | 2025-10-16 14:58:12 |
| OADP-4668 | Make using Velero CLI via velero deployment with caCert simple. | MODIFIED | Critical | 2025-10-14 09:03:33 |
| OADP-4051 | OADP install should be cluster scoped, should be able to manage multiple DPA's on cluster. | New | Blocker | 2025-10-16 15:08:25 |
| OADP-3971 | Additional secrets cannot be added to velero pod without restart | Dev Complete | Critical | 2025-10-09 11:40:10 |
| OADP-3759 | Velero shouldn't restore the restore-wait init container | POST | Normal | 2025-08-08 21:11:01 |
| OADP-2785 | Add possibility to configure "priorityClassName" for node-agent daemonset through DPA | In Progress | Major | 2025-10-16 15:41:44 |
0
## wnstb

| Issue Number | Description | Status | Priority | Date Updated |
|--------------|-------------|--------|----------|--------------|
| OADP-6796 | Validation: all BSL's point to a unique endpoint | New | Major | 2025-10-16 15:20:05 |
| OADP-6736 | Backup Repository controller may OOM kill Velero server when checking repo existence | In Progress | Undefined | 2025-10-16 17:07:30 |
| OADP-6735 | Behavioral change to default datamover behavior in go 1.25 | New | Undefined | 2025-09-24 21:28:30 |
| OADP-6732 | configMap validation in CLI should print the error when fails | New | Undefined | 2025-09-24 21:28:28 |
| OADP-6731 | Data mover expose diagnostic -- add events to diagnostic | In Progress | Undefined | 2025-10-16 17:02:14 |
| OADP-6729 | Deprecate Changing PVC selected-node feature | New | Undefined | 2025-09-24 21:28:28 |
| OADP-6726 | Check whether it's possible to remove VolumeSnapshotClass from the CSI B/R | In Progress | Undefined | 2025-10-16 16:56:13 |
| OADP-6725 | Integrate the node-agent-config documents together | In Progress | Undefined | 2025-10-16 16:55:02 |
| OADP-6724 | Repo cache volume -- DU deliver snapshot size to DD | In Progress | Undefined | 2025-10-16 16:54:56 |
| OADP-6723 | Repo cache volume -- PVB deliver snapshot size to PVR | In Progress | Undefined | 2025-10-16 16:54:49 |
| OADP-6722 | Repo cache volume -- Unified Repo support cache volume configuration | In Progress | Undefined | 2025-10-16 16:54:44 |
| OADP-6721 | Repo cache volume -- cache volume for data mover restore | In Progress | Undefined | 2025-10-16 16:54:38 |
| OADP-6720 | Repo cache volume -- cache volume for pod volume restore | In Progress | Undefined | 2025-10-16 16:56:04 |
| OADP-6693 | Address sparsify requirement post DM restore on ODF. | New | Undefined | 2025-09-15 21:22:36 |
| OADP-6360 | Add support for adding annotations to PodConfig | New | Major | 2025-09-10 15:20:37 |
| OADP-3039 | PodVolumeBackup/Restore CR status not marked as failed after backup/restore is failed | POST | Normal | 2025-09-10 15:24:02 |
0
## rh-ee-jvaikath

| Issue Number | Description | Status | Priority | Date Updated |
|--------------|-------------|--------|----------|--------------|
| OADP-6690 | operator-manager controller to track stuck velero objects | New | Normal | 2025-10-16 16:06:39 |
| OADP-6578 | CLI internationalization and localization support | Dev Complete | Undefined | 2025-08-15 15:14:57 |
| OADP-6577 | Backup metadata management and search | Dev Complete | Undefined | 2025-08-15 15:15:11 |
| OADP-6576 | CLI logging and audit trail functionality | Dev Complete | Undefined | 2025-08-15 15:15:23 |
| OADP-6575 | Backup encryption configuration through CLI | Dev Complete | Undefined | 2025-08-15 15:15:05 |
| OADP-6574 | CLI performance optimization and caching | Dev Complete | Undefined | 2025-08-15 15:15:07 |
| OADP-6573 | Integration with external monitoring systems | Dev Complete | Undefined | 2025-08-15 15:15:25 |
| OADP-6572 | Resource filtering and selective backup | Dev Complete | Undefined | 2025-08-15 15:14:52 |
| OADP-6571 | CLI plugin auto-update mechanism | Dev Complete | Undefined | 2025-08-15 15:15:14 |
| OADP-6570 | Cross-cluster backup and restore operations | Dev Complete | Undefined | 2025-08-15 15:14:34 |
| OADP-6569 | Backup retention policy configuration | Dev Complete | Undefined | 2025-08-15 15:14:36 |
| OADP-6568 | Volume snapshot management through CLI | Dev Complete | Undefined | 2025-08-15 15:14:49 |
| OADP-6567 | CLI output formatting options (JSON, YAML, table) | Dev Complete | Undefined | 2025-08-15 15:15:18 |
| OADP-6566 | Restore operation validation and dry-run | Dev Complete | Undefined | 2025-08-15 15:15:00 |
| OADP-6565 | Support for multiple cluster contexts | Dev Complete | Undefined | 2025-08-15 15:15:16 |
| OADP-6564 | CLI configuration file management | Dev Complete | Undefined | 2025-08-15 15:15:09 |
| OADP-6563 | Backup status monitoring and progress tracking | Dev Complete | Undefined | 2025-08-15 15:14:44 |
| OADP-6562 | Add support for backup scheduling through CLI | Dev Complete | Undefined | 2025-10-16 16:38:05 |
| OADP-6561 | CLI command validation and input sanitization | Dev Complete | Undefined | 2025-10-16 16:37:54 |
| OADP-6560 | Support for custom backup locations in CLI | Dev Complete | Undefined | 2025-10-16 16:37:51 |
| OADP-6559 | OADP CLI error handling improvements | Dev Complete | Undefined | 2025-10-16 16:38:03 |
| OADP-6558 | OADP CLI plugin installation and setup documentation | Dev Complete | Undefined | 2025-10-16 16:37:46 |
| OADP-6557 | NAR crud Support | Dev Complete | Undefined | 2025-10-16 16:37:59 |
| OADP-6556 | Review CACert config and testing | Dev Complete | Undefined | 2025-10-16 16:38:07 |
| OADP-6555 | oc oadp is defaulting to openshift-oadp namespace | Dev Complete | Undefined | 2025-08-15 15:15:12 |
| OADP-6554 | Add the plugin to oadp-operator operator hub page | Dev Complete | Undefined | 2025-10-16 16:37:45 |
| OADP-6553 | Implications of client - server version mismatch | Dev Complete | Undefined | 2025-10-16 16:38:02 |
| OADP-6552 | Help text on nabsl creation has wrong command info | Dev Complete | Undefined | 2025-10-16 16:37:57 |
| OADP-6551 | --all flag for nonadmin commands (delete) | Dev Complete | Undefined | 2025-10-16 16:37:48 |
| OADP-6550 | Rename version --client-only to version --client | Dev Complete | Undefined | 2025-10-16 16:37:55 |
| OADP-6549 | Do we need to use na? if it's not namespace where velero is running it should be by default non admin object | Dev Complete | Undefined | 2025-10-16 16:38:00 |
| OADP-6547 | Include must-gather in the oadp-cli | Dev Complete | Undefined | 2025-10-16 16:37:52 |
| OADP-6546 | oadp xyz help may give an example | Dev Complete | Undefined | 2025-10-16 16:37:49 |
| OADP-6545 | Support for setting namespace with -n flag when running velero commands | Dev Complete | Undefined | 2025-10-16 16:38:08 |
| OADP-5645 | OADP CSI Snapshot shows successful, but size is 0 bytes | MODIFIED | Critical | 2025-10-09 22:00:09 |
| OADP-3378 | Wrong/ misleading certificate error log for backup when certificate check is disabled | New | Normal | 2025-10-16 15:54:36 |
| OADP-3360 | PVC has a left out label related to volumeSnapshot after success FileSystem Restore | New | Minor | 2025-10-16 16:19:29 |
| OADP-2938 | Backup should immediately fail when nodeAgent pods are not running | MODIFIED | Normal | 2025-10-16 15:28:06 |
0
##  spampatt@redhat.com

| Issue Number | Description | Status | Priority | Date Updated |
|--------------|-------------|--------|----------|--------------|
| OADP-6846 | Support for labels/annotations on DataProtectionApplications | New | Critical | 2025-10-16 16:11:32 |
| OADP-6740 | [Upstream testing] VolumeSnapshotContent resources are left out in cluster with VGS path | New | Undefined | 2025-10-07 18:19:07 |
| OADP-6734 | maintenance jobs labels required for network-policies | In Progress | Undefined | 2025-10-16 17:05:12 |
| OADP-6733 | Maintenance Metrics | New | Undefined | 2025-10-16 17:03:58 |
| OADP-6696 | Backup and snapshot size reporting | New | Normal | 2025-09-17 16:30:43 |
| OADP-6694 | Repository maintenance jobs do not inherit tolerations from Velero deployment | Dev Complete | Major | 2025-10-16 15:46:40 |
| OADP-6688 | Velero scheduled backups accumulate in New state queue during extended blocking scenarios | Dev Complete | Major | 2025-10-16 15:48:00 |
| OADP-6582 | Implement VolumeGroupSnapshot (VGS) support in Velero | Dev Complete | Undefined | 2025-09-10 18:58:39 |
| OADP-6581 | VolumeGroupSnapshot Support Implementation | In Progress | Blocker | 2025-10-16 14:27:43 |
| OADP-6525 | Dramatic performance dropoff over time - Velero backup performance degradation | New | Undefined | 2025-08-13 19:04:12 |
| OADP-5171 | BSL status.message field shouldn't have the http response as output when bucket doesn't exist | POST | Minor | 2025-10-10 19:36:05 |
| OADP-4743 | DataMover restore partially fails when node selector spec is used | POST | Critical | 2025-10-08 18:56:23 |
0
## rhn-engineering-mpryc

| Issue Number | Description | Status | Priority | Date Updated |
|--------------|-------------|--------|----------|--------------|
| OADP-6583 | OADP Virtual Machine Data Protection (VMDP) Implementation | Refinement | Undefined | 2025-08-15 17:37:18 |
| OADP-6136 | Add compression to kopia / velero backups | In Progress | Undefined | 2025-08-01 17:25:45 |
| OADP-5235 | Velero runs as cluster-admin by default. | New | Normal | 2025-10-16 16:02:40 |
| OADP-5114 | Incompatibility of OADP with data mover restore | POST | Normal | 2025-09-10 15:14:34 |
| OADP-4855 | Kopia leaving cache on worker node | New | Major | 2025-10-16 15:14:20 |
| OADP-4289 | Velero fails to patch managed fields on namespace resources which causing restore to partially fail | ASSIGNED | Normal | 2025-10-08 17:58:13 |
| OADP-3692 | Make dpa.spec.configuration.velero.defaultVolumesToFSBackup flag identical to backup spec | ASSIGNED | Minor | 2025-10-08 18:51:42 |
| OADP-3471 | Update any timeout fields to 4h0m0s type | ASSIGNED | Undefined | 2025-10-16 16:24:40 |
0
## sseago

| Issue Number | Description | Status | Priority | Date Updated |
|--------------|-------------|--------|----------|--------------|
| OADP-6737 | Concurrent backup processing | In Progress | Undefined | 2025-10-16 17:09:33 |
| OADP-6579 | Concurrent Backup Processing Implementation | In Progress | Blocker | 2025-10-16 14:27:20 |
| OADP-5486 | Handle - Retry Generate Name | New | Normal | 2025-10-16 16:03:27 |
| OADP-4589 | Dataupload object reporting improvements | In Progress | Major | 2025-10-16 16:52:46 |

