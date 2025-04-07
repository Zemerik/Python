import psutil
import time
import logging

logging.basicConfig(filename="system.log", level=logging.INFO)

def monitor_system(interval=300):
    while True:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        
        status = (
            f"CPU: {cpu}% | "
            f"Memory: {memory}% | "
            f"Disk: {disk}%"
        )
        
        logging.info(status)
        
        if cpu > 80 or memory > 80 or disk > 90:
            logging.warning("Critical system overload!")
        
        time.sleep(interval)

if __name__ == "__main__":
    monitor_system()