import schedule
import time
from datetime import datetime

def system_cleanup():
    print(f"{datetime.now()}: Performing cleanup...")
    # Add actual cleanup logic here

def reminder(message):
    print(f"{datetime.now()}: REMINDER - {message}")

# Schedule tasks
schedule.every().day.at("23:30").do(system_cleanup)
schedule.every(45).minutes.do(reminder, "Take a break!")

while True:
    schedule.run_pending()
    time.sleep(1)