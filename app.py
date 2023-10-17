from selenium import webdriver
import time

website_url = 'https://getsetoa.tech/'
open_interval = 0.1  
close_delay = 0.1  

driver = webdriver.Chrome() 

while True:
    driver.get(website_url)
    time.sleep(close_delay)
    driver.close()

    time.sleep(open_interval)
    
    driver = webdriver.Chrome()

driver.quit()