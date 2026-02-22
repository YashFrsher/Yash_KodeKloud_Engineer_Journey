# Python-Based Linux Server Monitoring Agent
import argparse
import logging
import time
from logging.handlers import RotatingFileHandler

import psutil

## Logging Configuration.

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.handlers.clear()
file_handler = RotatingFileHandler("server_monitor.log", maxBytes= 5 *1024 * 1024, backupCount=3)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Default threshold Value.
thresholds = {
    "cpu": 80,
    "memory": 75,
    "disk": 85
}

# Function 1: This Collects the system level metrics like CPU, Memory and Disk
def get_system_metrics():
    metrics = {}
    # System metrics
    cpu_percent = psutil.cpu_percent()
    virtual_memory_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")
    metrics["cpu"] = cpu_percent
    metrics["memory"] = virtual_memory_usage.percent
    metrics["disk"] = disk_usage.percent
    logger.debug(f"Collected metrics: {metrics}")  # this will only get printed if --debug flag is passed when running the script.
    return metrics

# Function 2: This function compares the metrics collect against the threshold value and logs it in the log file.
def check_threshold(metrics,threshold):
    for key, value in metrics.items():
        if key in threshold:
            if value >= threshold[key]:
                logger.warning(f"{key} exceeds threshold. Current = {value}% Threshold Limit = {threshold[key]}%")
            else:
                logger.info(f"{key} is below threshold. Current = {value}% Threshold Limit = {threshold[key]}%")
        else:
            logger.error(f"{key} is not a managed metric")
            pass
# Function 3: This function takes the custom CLI inputs to check the metrics with custom threshold.
def cli_arguments():
    parser = argparse.ArgumentParser(description="Server Health Monitoring Tool")
    parser.add_argument("--cpu", type=float, help="CPU threshold value")
    parser.add_argument("--memory", type=float, help="CPU threshold value")
    parser.add_argument("--disk", type=float, help="CPU threshold value")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    return parser.parse_args()

# Function 4: This function calls the above functions and also set the logging level to debug when flag is used.
def main():
    args = cli_arguments()
    if args.cpu is not None:
        thresholds["cpu"] = args.cpu
    if args.memory is not None:
        thresholds["memory"] = args.memory
    if args.disk is not None:
        thresholds["disk"] = args.disk
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    check_threshold(get_system_metrics(), threshold=thresholds)

# Function 5: This function runs the main function in a loop. We get the metrics every 5 seconds.
if __name__ == "__main__":
    while True:
        main()
        time.sleep(5)