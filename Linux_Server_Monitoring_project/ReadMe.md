# 🖥️ Python-Based Linux Server Monitoring Agent

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![Logging](https://img.shields.io/badge/Logging-RotatingFileHandler-orange)
![Status](https://img.shields.io/badge/Project-Weekend%20Mini%20Project-success)

------------------------------------------------------------------------

## 📌 Project Overview

A lightweight Linux monitoring agent built using Python.\
This tool collects system metrics, compares them against configurable
thresholds, and logs structured alerts with automatic log rotation.

------------------------------------------------------------------------

# 🏗️ Architecture Diagram

                        +---------------------+
                        |   CLI Arguments     |
                        | (--cpu, --memory,   |
                        |  --disk, --debug)   |
                        +----------+----------+
                                   |
                                   v
                        +---------------------+
                        |       main()        |
                        |  - Override config  |
                        |  - Set log level    |
                        +----------+----------+
                                   |
                                   v
                        +---------------------+
                        | get_system_metrics  |
                        |  - CPU (psutil)     |
                        |  - Memory           |
                        |  - Disk             |
                        +----------+----------+
                                   |
                                   v
                        +---------------------+
                        | check_threshold()   |
                        |  Compare vs limits  |
                        +----------+----------+
                                   |
                                   v
                        +---------------------+
                        |       Logger        |
                        |  INFO / WARNING     |
                        +----+-----------+----+
                             |           |
                             v           v
                   +---------------+   +---------------+
                   | Console       |   | Rotating File |
                   | StreamHandler |   | server_monitor|
                   +---------------+   +---------------+

------------------------------------------------------------------------

# 🚀 Features

-   CPU, Memory, and Disk Monitoring
-   CLI-Based Threshold Override
-   Structured Logging
-   Debug Mode
-   Log Rotation by Size
-   Continuous Monitoring Loop

------------------------------------------------------------------------

# 📦 Requirements

-   Python 3.x
-   Linux OS
-   psutil library

Install dependency:

``` bash
pip install psutil
```

------------------------------------------------------------------------

# 📝 Code Structure Explanation

## 1️⃣ Logging Configuration

-   Creates root logger
-   Clears existing handlers
-   Adds:
    -   RotatingFileHandler (5MB rotation, 3 backups)
    -   Console StreamHandler
-   Uses structured format:

```{=html}
<!-- -->
```
    %(asctime)s | %(levelname)s | %(message)s

This ensures production-grade logging.

------------------------------------------------------------------------

## 2️⃣ Threshold Configuration

Default thresholds:

    cpu: 80%
    memory: 75%
    disk: 85%

These can be overridden via CLI.

------------------------------------------------------------------------

## 3️⃣ Metric Collection -- `get_system_metrics()`

Uses `psutil` to fetch:

-   CPU usage %
-   Memory usage %
-   Root disk usage %

Returns dictionary:

    {
      "cpu": value,
      "memory": value,
      "disk": value
    }

------------------------------------------------------------------------

## 4️⃣ Threshold Comparison -- `check_threshold()`

Logic:

-   If value \>= threshold → WARNING
-   If value \< threshold → INFO
-   If metric not managed → ERROR

This provides severity-based monitoring.

------------------------------------------------------------------------

## 5️⃣ CLI Argument Handling -- `cli_arguments()`

Supported flags:

-   --cpu
-   --memory
-   --disk
-   --debug

--debug enables DEBUG level logging.

------------------------------------------------------------------------

## 6️⃣ Continuous Monitoring

Runs every 5 seconds using:

    while True:
        main()
        time.sleep(5)

Simulates a lightweight monitoring agent.

------------------------------------------------------------------------

# 🧪 How To Use

### ▶️ Default Run

    python monitor.py

### ▶️ Custom Thresholds

    python monitor.py --cpu 70 --memory 60 --disk 80

### ▶️ Enable Debug Mode

    python monitor.py --debug

------------------------------------------------------------------------

# 📁 Log Output

-   Printed in console
-   Written to `server_monitor.log`
-   Rotates automatically at 5MB
-   Keeps 3 backup files

------------------------------------------------------------------------

# 🎯 Key Concepts Demonstrated

-   Data Types (dict, float)
-   Conditionals
-   Loops
-   Functions
-   CLI Parsing
-   Logging Levels
-   Log Rotation
-   Continuous Monitoring

------------------------------------------------------------------------

# 📌 Summary

This project demonstrates production-inspired DevOps scripting
practices:

✔ Structured logging\
✔ Log rotation safety\
✔ Threshold-based alerting\
✔ Runtime configurability\
✔ Clean modular design
