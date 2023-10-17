import logging
import tkinter as tk
from selenium import webdriver
import time
import socket

# Set up logging to save output to a text file
logging.basicConfig(filename='selenium_log.txt', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

open_interval = 0.2  # Set the interval for opening the site (in seconds)

# Create a function to update and display information in a pop-up window
def update_info():
    # Get the local IP address and port of the system
    local_ip = socket.gethostbyname(socket.gethostname())
    local_port = driver.service.service_url.split(':')[-1]
    
    log_text = f'Iteration {iteration_count + 1}\n'
    log_text += f'Local IP Address: {local_ip}\n'
    log_text += f'Local Port: {local_port}\n'

    logging.info(log_text)
    info_label.config(text=log_text)
    
    # Open a pop-up window
    popup = tk.Toplevel()
    popup.title("Selenium Log Info")
    popup.geometry("400x200")
    
    log_label = tk.Label(popup, text=log_text, font=("Arial", 12))
    log_label.pack(padx=20, pady=20)
    
driver = webdriver.Chrome() 

iteration_count = 0

# Create a tkinter window to display information
root = tk.Tk()
root.title("Selenium Log Info")

info_label = tk.Label(root, text="Information will be displayed here.", font=("Arial", 12))
info_label.pack(padx=20, pady=20)

# Create a button to manually trigger information display
info_button = tk.Button(root, text="Display Info", command=update_info)
info_button.pack()

while True:
    # Automatically display information in a pop-up window
    update_info()
    
    driver.get('https://getsetoa.tech/')  # Load the website
    time.sleep(2)  # Add some delay for demonstration
    driver.quit()
    
    time.sleep(open_interval)
    
    driver = webdriver.Chrome()
    iteration_count += 1

root.mainloop()  # Start the tkinter main loop
