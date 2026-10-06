# Local GitOps Multi-Cluster Setup (KinD + Flux CD + Kustomize + MongoDB)

This project manages a local multi-cluster environment (`dev` and `prod`) using Kubernetes-in-Docker (Kind), GitOps via Flux CD, and persistent MongoDB storage.

## Architecture

- **Control Plane & Workers:** 1 Control Plane + 3 Worker Nodes per cluster.
- **GitOps Operator:** Flux CD tracking GitLab repo `gitops-fleet`.
- **Database:** MongoDB StatefulSet mapped to host storage (`/tmp/kind-data/...`).
- **UI:** Mongo Express Web UI exposed via Kind NodePort mappings.
  - **Dev UI:** `http://localhost:8081`
  - **Prod UI:** `http://localhost:8082`

## Prerequisites

- Docker
- Kind (`brew install kind` or binary download)
- kubectl
- flux CLI (`brew install fluxcd/tap/flux`)
- GitLab account & PAT (`export GITLAB_TOKEN="glpat-..."`)

## Quick Start

### 1. Create Local Host Mount Directories
```bash
mkdir -p /tmp/kind-data/dev-mongo /tmp/kind-data/prod-mongo
chmod 777 /tmp/kind-data/dev-mongo /tmp/kind-data/prod-mongo