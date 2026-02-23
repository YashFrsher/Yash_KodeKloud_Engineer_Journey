# 🚀 Terraform Kubernetes WebApp Deployment

![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?style=flat&logo=terraform)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?style=flat&logo=kubernetes)
![Service](https://img.shields.io/badge/NodePort-Service-green?style=flat)
![Replicas](https://img.shields.io/badge/Replicas-4-orange?style=flat)

------------------------------------------------------------------------

## 📌 Project Overview

This project demonstrates how to deploy a containerized web application
to Kubernetes using **Terraform Infrastructure as Code (IaC)**.

### 🔹 What This Project Includes

-   Kubernetes Deployment (4 replicas)
-   ReplicaSet managed automatically
-   NodePort Service exposure
-   Dynamic label & selector referencing
-   End-to-end Terraform workflow validation

📂 Full Terraform configuration is available in the `.tf` files inside
this repository.

------------------------------------------------------------------------

# 🏗 Architecture

> Keep `architecture.png` in the root of this repository.

![Architecture Diagram](./architecture.png)

### 🔎 Architecture Flow

Terraform → Kubernetes Provider → Deployment → ReplicaSet → Pods (4
replicas)\
Service (NodePort) selects Pods via labels

------------------------------------------------------------------------

# ❓ Problem Statements & Solutions

## 1️⃣ How does Terraform connect to Kubernetes?

Used the official `hashicorp/kubernetes` provider with kubeconfig
authentication.

## 2️⃣ How are multiple replicas created?

Deployment configured with `replicas = 4`.

## 3️⃣ How is the application exposed?

NodePort Service mapping port `8080` to `node_port = 30080`.

## 4️⃣ How does Service dynamically select Pods?

Used Terraform resource reference:

`kubernetes_deployment.frontend.spec[0].template[0].metadata[0].labels.name`

------------------------------------------------------------------------

# 🧪 Validation & Testing

## 🔹 Terraform Workflow

``` bash
terraform init
terraform validate
terraform plan
terraform apply
```

## 🔹 Kubernetes Verification

``` bash
kubectl get deployments
kubectl get pods
kubectl get svc
kubectl describe svc webapp-service
```

✔ Verified 4 running pods\
✔ Verified Service selector matches Pod labels\
✔ Verified endpoints successfully registered

------------------------------------------------------------------------

# ⚠️ Errors Faced (One-Line Learnings)

  -----------------------------------------------------------------------
  Error                         Learning
  ----------------------------- -----------------------------------------
  Unsupported block type        Terraform expects `port` block, not
  `ports`                       `ports`.

  Missing `container_port`      Must define container_port inside port
                                block.

  Used `containerPort`          Terraform requires snake_case
                                (`container_port`).

  Deprecated deployment         Should migrate to
  resource                      `kubernetes_deployment_v1`.

  Used `nodePort`               Must use `node_port` in Terraform syntax.

  No endpoints registered       Service selector must match Pod template
                                labels.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 🧠 Key Learnings

-   Terraform HCL differs from Kubernetes YAML
-   Services select Pods, not Deployments
-   Label consistency is critical
-   Provider validation catches schema issues early
-   Debugging requires both Terraform and kubectl

------------------------------------------------------------------------

# 🎯 Final Outcome

✔ Infrastructure deployed using Terraform\
✔ 4 replicas running successfully\
✔ NodePort Service exposed\
✔ Proper label-based networking\
✔ End-to-end IaC workflow implemented

------------------------------------------------------------------------

**Infrastructure as Code • Kubernetes • DevOps Practice**
