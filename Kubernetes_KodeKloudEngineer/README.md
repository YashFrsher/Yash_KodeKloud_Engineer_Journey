
# 🚀 Kubernetes Hands-On Labs – 40 Real Use Cases

![Kubernetes](https://img.shields.io/badge/Kubernetes-Production%20Practice-326CE5?logo=kubernetes&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-Hands%20On-success)
![YAML](https://img.shields.io/badge/YAML-Infrastructure-blue)
![Containers](https://img.shields.io/badge/Containers-Docker%20%7C%20K8s-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-Troubleshooting-red)

---

## 📌 Overview

This repository documents my end‑to‑end Kubernetes journey through **40 practical DevOps scenarios**.  
Each use case simulates real production deployments, failures, and debugging workflows.

This project focuses on:

- Real infrastructure building
- Application deployment
- Storage & networking
- Configuration management
- Secrets handling
- Multi‑container architecture
- Production troubleshooting

This is operational Kubernetes practice — not theory.

---

## 🧠 Skills Demonstrated

- Pods, Deployments, ReplicaSets
- Rolling updates & rollbacks
- Services & DNS routing
- PersistentVolumes & PersistentVolumeClaims
- ConfigMaps & Secrets
- Init containers & Sidecars
- CronJobs & Jobs
- Multi-tier applications (LAMP / LEMP)
- PHP + Nginx + MySQL stacks
- Redis caching
- Drupal deployment
- Jenkins & Grafana services
- Shared volumes with emptyDir
- Environment variable injection
- Secret mounting & security best practices
- Debugging container failures
- Storage validation & persistence testing

---

## 🏆 Top Production Use Cases

### 1. LAMP Stack (PHP + MySQL)

Multi-container pod with:

- PHP Apache
- MySQL database
- Secrets for credentials
- ConfigMap for php.ini
- NodePort exposure

Key learning:

- subPath ConfigMap mounting
- secret env injection
- PHP ↔ MySQL connectivity debugging

---

### 2. Nginx + PHP-FPM Architecture

Reverse proxy + backend stack with:

- FastCGI routing
- shared volumes
- custom nginx.conf
- 502 debugging
- multi-container networking

---

### 3. Persistent MySQL with PV/PVC

Stateful storage lab covering:

- PersistentVolume lifecycle
- PVC binding
- database persistence validation
- hostPath storage
- real data survival tests

---

### 4. Init Container Pattern

Sequential container workflow:

- init container prepares filesystem
- shared emptyDir volume
- main container consumes prepared data

---

### 5. Sidecar Logging Pattern

Separation of concerns architecture:

- nginx app container
- logging sidecar
- shared log volume
- continuous log streaming

---

## 🔧 Troubleshooting Highlights

Real production-style failures debugged:

- ImagePullBackOff
- CrashLoopBackOff
- service selector mismatch
- YAML indentation errors
- missing volumes
- nginx 502 backend failures
- PHP database connection errors
- secret misconfigurations
- DNS resolution failures

Tools used:

```
kubectl logs
kubectl describe
kubectl exec
kubectl get endpoints
kubectl rollout history
kubectl rollout undo
```

---

## ✅ Validation Strategy

Every lab was validated beyond “Running” state:

- container shell inspection
- DB login tests
- file persistence checks
- environment variable validation
- service connectivity verification
- endpoint inspection

This mirrors real SRE workflows.

---

## 🎯 Outcome

After completing all 40 labs I can confidently:

- design Kubernetes workloads from scratch
- troubleshoot broken deployments
- wire multi-container systems
- manage secure configuration
- validate persistent storage
- operate production-style clusters

This repository is a practical Kubernetes playbook.

---

## 📂 Repository Structure

Each folder contains:

- YAML manifests
- execution commands
- troubleshooting notes
- validation steps
- working solutions

The README summarizes the journey.  
The folders contain the implementation detail.

---

## 🚀 Next Goals

Planned extensions:

- Helm packaging
- Kubernetes probes
- StatefulSets
- Ingress controllers
- Observability stack
- GitOps pipelines
- CI/CD integration

---

If you are reviewing this repo as a recruiter or engineer:

👉 This demonstrates operational Kubernetes skills, not just YAML writing.
