# 🚀 LAMP Stack Deployment Using Terraform + Docker

## 📌 Project Overview

This project provisions a production-style **LAMP stack** using:

-   Terraform (Infrastructure as Code)
-   Docker Provider
-   Custom Docker Images
-   Custom Docker Network
-   Persistent Database Volume

The infrastructure simulates real-world production behavior including:

-   Multi-container deployment
-   Network isolation
-   Persistent storage
-   Environment-driven configuration
-   Controlled container dependencies

------------------------------------------------------------------------

## 🏗 Architecture

Terraform provisions the following:

-   Custom PHP-HTTPD Image
-   Custom MariaDB Image
-   phpMyAdmin Container
-   Private Docker Network
-   Persistent Docker Volume

All application containers are attached to a custom Docker network for
secure internal communication.

------------------------------------------------------------------------

## 🧱 Infrastructure Components

### 1️⃣ PHP Web Server

-   Image: `php-httpd:challenge`
-   Built from: `lamp_stack/php_httpd`
-   Container Name: `webserver`
-   Hostname: `php-httpd`
-   Port: `80`
-   Volume Mount:
    -   Host:
        `/root/code/terraform-challenges/challenge2/lamp_stack/website_content/`
    -   Container: `/var/www/html`

------------------------------------------------------------------------

### 2️⃣ MariaDB Database

-   Image: `mariadb:challenge`
-   Built from: `lamp_stack/custom_db`
-   Container Name: `db`
-   Hostname: `db`
-   Port: `3306`
-   Environment Variables:
    -   MYSQL_ROOT_PASSWORD
    -   MYSQL_DATABASE
-   Persistent Volume:
    -   `mariadb-volume` → `/var/lib/mysql`

------------------------------------------------------------------------

### 3️⃣ phpMyAdmin Dashboard

-   Image: `phpmyadmin/phpmyadmin`
-   Container Name: `db_dashboard`
-   Hostname: `phpmyadmin`
-   Port: `8081`
-   Linked to MariaDB container

------------------------------------------------------------------------

### 4️⃣ Docker Network

-   Name: `my_network`
-   Enables internal DNS-based communication
-   Isolates application stack from default bridge network

------------------------------------------------------------------------

### 5️⃣ Persistent Storage

-   Docker Volume: `mariadb-volume`
-   Ensures database data persists across container restarts

------------------------------------------------------------------------

## 🔐 Production Behaviors Simulated

  Feature                            Implementation
  ---------------------------------- ------------------------------
  Network Isolation                  Custom Docker bridge network
  Persistent Storage                 Docker volume
  Config via Environment Variables   Terraform variables
  Image Build Automation             docker_image resource
  Dependency Management              depends_on
  Port Binding Control               internal/external mapping
  Resource Labeling                  Metadata tagging

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── main.tf
    ├── network.tf
    ├── mariadb-image.tf
    ├── php-httpd-image.tf
    ├── containers.tf
    ├── variables.tf
    ├── dev.tfvars
    ├── DockerWithTerraform.png
    └── lamp_stack/

------------------------------------------------------------------------

## ▶️ How To Deploy

### 1️⃣ Initialize Terraform

    terraform init

### 2️⃣ Validate Configuration

    terraform validate

### 3️⃣ Review Execution Plan

    terraform plan -var-file="dev.tfvars"

### 4️⃣ Apply Infrastructure

    terraform apply --auto-approve -var-file="dev.tfvars"

------------------------------------------------------------------------

## 🔎 Post-Deployment Validation

### Verify Running Containers

    docker ps

### Verify Network

    docker network inspect my_network

### Verify Volume

    docker volume ls
    docker volume inspect mariadb-volume

### Access Web Server

    http://<server-ip>:80

### Access phpMyAdmin

    http://<server-ip>:8081

Login Credentials: - Username: root - Password: (value defined in
tfvars)

------------------------------------------------------------------------

## 🧠 Key Learning Outcomes

-   Terraform Docker provider usage
-   Multi-container orchestration
-   Custom image builds
-   Environment variable injection
-   Volume persistence
-   Network-based service communication
-   Production simulation patterns

------------------------------------------------------------------------

## 🧹 Cleanup

To destroy all resources:

    terraform destroy --auto-approve -var-file="dev.tfvars"

------------------------------------------------------------------------

### Author

Deployed and managed using Terraform & Docker for infrastructure
simulation and DevOps practice.
