# Local Multi-OS Ansible & Kubernetes Lab

This repository provisions a 3-node local lab environment using Docker containers running different Linux distributions (Ubuntu, Debian, Rocky Linux) and automates the installation of **tmux** and **Kubernetes tooling (`kubelet`, `kubeadm`, `kubectl`)** via Ansible.

## Architecture

| Container Name | OS Distribution | Exposed SSH Port | Default User | Default Password |
| :--- | :--- | :--- | :--- | :--- |
| `node-ubuntu` | Ubuntu | `2221` | `linuxserver` | `berkayalan123` |
| `node-debian` | Debian | `2222` | `linuxserver` | `berkayalan123` |
| `node-rocky` | Rocky Linux 9 | `2223` | `root` | `berkayalan123` |

---

## Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose
- [Ansible](https://docs.ansible.com/) installed on host machine
- `sshpass` utility installed locally (required for password-based SSH authentication in Ansible):
  - Ubuntu/Debian: `sudo apt install sshpass`
  - macOS: `brew install hudochenkov/sshpass/sshpass`

---

## Quick Start

### 1. Spin up the containers
```bash
docker compose up -d
```

### Connect to machines

# Get the IPs

docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q)

# Ubuntu Node
ssh linuxserver@127.0.0.1 -p 2221

# Debian Node
ssh linuxserver@127.0.0.1 -p 2222

# Rocky Linux Node
ssh root@127.0.0.1 -p 2223

# Check if k8 installed
kubectl version --client

## AWS Provision

Install the collection
`ansible-galaxy collection install amazon.aws`

Run the provisioning
`ansible-playbook aws-provision.yaml`

All the details about the collection
https://docs.ansible.com/projects/ansible/latest/collections/amazon/aws/s3_bucket_module.html#ansible-collections-amazon-aws-s3-bucket-module

To check the lint
`ansible-lint aws-provision.yaml`

## Notes

- How to Use Ansible when with ansible_os_family?

https://oneuptime.com/blog/post/2026-02-21-how-to-use-ansible-when-with-ansible-os-family/view

- 