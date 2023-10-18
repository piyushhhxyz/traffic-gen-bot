import schedule
import time
import subprocess

# Define the time when you want the Selenium script to run daily
scheduled_time = "04:30"

def run_selenium_script():
    # Run the Selenium script as a separate process
    script_path = "path_to_selenium_script.py"  # Replace with the actual path
    subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
# Schedule the script to run daily at the specified time
schedule.every().day.at(scheduled_time).do(run_selenium_script)

while True:
    schedule.run_pending()
    time.sleep(1)
