from selenium import webdriver
import time
import pyautogui

website_url = 'https://getsetoa.tech/'
open_interval = 0.1
close_delay = 0.1

max_duration_seconds = 2 * 60 * 60 

start_time_fixed = time.strptime("04:30:00", "%H:%M:%S")

max_iterations_per_round = 10

driver = webdriver.Chrome() 

with open('logs.txt', 'a') as log_file:
    start_time = time.time()

    round_number = 1

    while True:
        current_time = time.time()
        elapsed_time_seconds = current_time - start_time

        if elapsed_time_seconds >= max_duration_seconds:
            break

        current_round_start_time = time.strftime('%I.%M %p', start_time_fixed)
        log_file.write(f'Round {round_number} - Start Time: {current_round_start_time}\n')

        for iteration in range(1, max_iterations_per_round + 1):
            current_time = time.strftime('%dth %b : %I.%M %p', time.localtime())
            log_entry = f'Iteration {iteration} - {current_time}\n'
            log_file.write(log_entry)

            driver.get(website_url)
            time.sleep(close_delay)
            driver.close()

            time.sleep(open_interval)

            driver = webdriver.Chrome()

        log_file.write('\n\n')

        pyautogui.move(1, 1)

        elapsed_time_seconds = time.time() - start_time

        if elapsed_time_seconds < max_duration_seconds:
            print("Pausing for 5 minutes...")
            time.sleep(5 * 60) 
            start_time = time.time()  
            round_number += 1  


driver.quit()
