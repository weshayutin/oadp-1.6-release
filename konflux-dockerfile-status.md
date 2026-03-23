# OADP 1.6 - konflux.Dockerfile Status

> Last updated: 2026-03-23
>
> Reference Dockerfile: [openshift/velero-plugin-for-aws `oadp-1.6`](https://github.com/openshift/velero-plugin-for-aws/blob/oadp-1.6/konflux.Dockerfile)

## Summary

| Status | Count |
|--------|-------|
| Done (branch + Dockerfile merged) | 9 |
| PR Open targeting oadp-1.6 | 4 |
| PR Open targeting oadp-dev only (needs oadp-1.6 PR) | 1 |
| No PR yet (branch exists, Dockerfile missing) | 1 |
| Branch `oadp-1.6` missing | 3 |
| Skipped / commented out | 2 |

---

## Done - No Action Needed

| Repo | Notes |
|------|-------|
| [openshift/velero-plugin-for-aws](https://github.com/openshift/velero-plugin-for-aws/tree/oadp-1.6) | **Reference** implementation |
| [openshift/oadp-operator](https://github.com/openshift/oadp-operator/tree/oadp-1.6) | Dockerfile merged |
| [openshift/velero](https://github.com/openshift/velero/tree/oadp-1.6) | Dockerfile merged (was PR [#487](https://github.com/openshift/velero/pull/487)) |
| [openshift/velero-plugin-for-microsoft-azure](https://github.com/openshift/velero-plugin-for-microsoft-azure/tree/oadp-1.6) | Dockerfile merged |
| [openshift/velero-plugin-for-legacy-aws](https://github.com/openshift/velero-plugin-for-legacy-aws/tree/oadp-1.6) | Dockerfile merged |
| [openshift/openshift-velero-plugin](https://github.com/openshift/openshift-velero-plugin/tree/oadp-1.6) | Dockerfile merged (was PR [#383](https://github.com/openshift/openshift-velero-plugin/pull/383)) |
| [openshift/velero-plugin-for-gcp](https://github.com/openshift/velero-plugin-for-gcp/tree/oadp-1.6) | Dockerfile merged |
| [migtools/kubevirt-datamover-controller](https://github.com/migtools/kubevirt-datamover-controller/tree/oadp-1.6) | Dockerfile merged (was PR [#37](https://github.com/migtools/kubevirt-datamover-controller/pull/37)) |
| [migtools/oadp-vm-file-restore](https://github.com/migtools/oadp-vm-file-restore/tree/oadp-1.6) | Dockerfile merged (uses golang_1.24, consider updating to 1.25) |

---

## PRs Open - Targeting `oadp-1.6`

| Repo | PR | CI Status | Action |
|------|----|-----------|--------|
| [openshift/oadp-must-gather](https://github.com/openshift/oadp-must-gather/tree/oadp-1.6) | [#87](https://github.com/openshift/oadp-must-gather/pull/87) | images: SUCCESS, tide: SUCCESS | **Ready to merge** |
| [migtools/oadp-non-admin](https://github.com/migtools/oadp-non-admin/tree/oadp-1.6) | [#332](https://github.com/migtools/oadp-non-admin/pull/332) | images: PENDING, snyk: SUCCESS | Waiting on CI |
| [migtools/filebrowser](https://github.com/migtools/filebrowser/tree/oadp-1.6) | [#7](https://github.com/migtools/filebrowser/pull/7) | images: SUCCESS, tide: SUCCESS, Lint Frontend: **FAILURE**, Validate Title: **FAILURE** | Pre-existing GH Actions failures; prow checks pass |
| [migtools/kubevirt-datamover-plugin](https://github.com/migtools/kubevirt-datamover-plugin/tree/oadp-1.6) | [#9](https://github.com/migtools/kubevirt-datamover-plugin/pull/9) | images: **FAILURE**, tide: PENDING | CI failure, needs investigation |

---

## PR Open - Targeting `oadp-dev` Only (needs oadp-1.6 PR)

| Repo | PR (oadp-dev) | oadp-1.6 PR? | Notes |
|------|---------------|--------------|-------|
| [migtools/oadp-vmdp](https://github.com/migtools/oadp-vmdp/tree/oadp-1.6) | [#5](https://github.com/migtools/oadp-vmdp/pull/5) | **None** | oadp-1.6 branch exists, needs separate PR |

---

## No PR Yet - Branch Exists, Dockerfile Missing

| Repo | Action Needed |
|------|---------------|
| [migtools/oadp-cli](https://github.com/migtools/oadp-cli/tree/oadp-1.6) | Create and submit konflux.Dockerfile PR to oadp-1.6 |

---

## Branch `oadp-1.6` Missing

| Repo | Existing Branches | Action Needed |
|------|-------------------|---------------|
| [migtools/kubevirt-velero-plugin](https://github.com/migtools/kubevirt-velero-plugin) | `main`, `release-v0.1` .. `release-v0.8` | Create `oadp-1.6` branch, then add konflux.Dockerfile |
| [openshift/hypershift-oadp-plugin](https://github.com/openshift/hypershift-oadp-plugin) | `main`, `oadp-1.4`, `oadp-1.5` | Create `oadp-1.6` branch, then add konflux.Dockerfile |
| [migtools/kubevirt-datamover-monitor](https://github.com/migtools/kubevirt-datamover-monitor) | `oadp-dev` only | Create `oadp-1.6` branch, then add konflux.Dockerfile |

---

## Skipped

| Repo | Reason |
|------|--------|
| [migtools/kopia](https://github.com/migtools/kopia) | Commented out in OADP-1.6-repos |
| [openshift/restic](https://github.com/openshift/restic) | Commented out in OADP-1.6-repos |
| [migtools/kubevirt-velero-annotation-remover](https://github.com/migtools/kubevirt-velero-annotation-remover) | Repository not found (404) |
