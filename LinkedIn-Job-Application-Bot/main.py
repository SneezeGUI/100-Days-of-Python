import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

#load .env variables
load_dotenv()
phone = os.getenv('PHONE')
password = os.getenv('PASSWORD')

# Set options to keep the Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initiate a driver with our options
driver = webdriver.Chrome(options=chrome_options)
# URL To Load
driver.get(url='https://www.linkedin.com/jobs/search/?currentJobId=4118970938&f_AL=true&geoId=103644278&keywords=python%20developers&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')
time.sleep(3)  # Let's give some time for the page to fully load
try:
    sign_in_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sign_in_button.click() # click on the sign in button
except NoSuchElementException or ElementNotInteractableException:
    print('Element not found')

try:
    user_input = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]') # Get USER login field
    user_input.send_keys(phone) #enter user phone from .env
    time.sleep(1)

    password_input = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]') # Get PAssword login field
    password_input.send_keys(password) #enter user password from .env
    time.sleep(1)

    login_button = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button') # get login button
    login_button.click() # submit login form by clicking login button

    time.sleep(5) #wait for page to load

    # Apply for first job listing
    apply_button = driver.find_element(By.XPATH, value='//*[@id="ember57"]') #find apply button
    apply_button.click() #click apply button
    time.sleep(3)

    next_button = driver.find_element(By.XPATH, value='//*[@id="ember394"]')
    next_button.click()
    time.sleep(1)
    next_button.click()


except NoSuchElementException or ElementNotInteractableException:
    print('Element not found')
