import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

# Set options to keep the Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initiate a driver with our options
driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://orteil.dashnet.org/cookieclicker/')  # Load Cookie Clicker game page into the browser
time.sleep(2)  # Let's give some time for the page to fully load

# Choose English language
english = driver.find_element(By.ID, value='langSelect-EN')
english.click()
time.sleep(3)

##LOAD SAVE##
# with open('SaveGames/SneezeBakery.txt', 'w') as save:
#     options_button = driver.find_element(By.XPATH, value='//*[@id="prefsButton"]/div')
#     options_button.click()
#     time.sleep(10)

# Find the cookie element that we will be clicking on
cookie = driver.find_element(By.ID, value='bigCookie')

# Get upgrade item ids from the game page
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div .price")
item_ids = [item.get_attribute("id") for item in items]  # Extract all ids of the upgrade items
print(item_ids)

timeout = time.time() + 5  # Set a timeout to buy upgrades every 5 seconds
five_min = time.time() + 60*5  # Set a limit of 5 minutes for the bot's operation
while True:
    for i in range(100, 0, -1):
        cookie.click()


    if time.time() > timeout:  # If it's been 5 seconds since we last clicked on an upgrade button

        available_upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")  # Check for all available upgrades that we can afford
        try:
            available_powerups = driver.find_element(By.XPATH, value='//*[@id="upgrade0"]')
            available_powerups.click()
        except NoSuchElementException or ElementNotInteractableException:
            print('there was an error clicking powerups')

        highest = None
        available_cookies = float(driver.find_element(By.ID, "cookies").text.split()[0].replace(",", ".")) # Get current cookies count
        # print(available_cookies)
        for upgrade in available_upgrades:  # Check for the most expensive upgrade we can currently afford
            try:
                upgrade_cost = float(upgrade.find_element(By.CLASS_NAME, "price").text.replace(",", "."))
            except ValueError:
                print('Bot is not capable of handling numbers this large yet')
            #     million = 10**6
            #     upgrade_cost = float(upgrade.find_element(By.CLASS_NAME, value='price').text.split()[0]*million)

            if available_cookies >= upgrade_cost:
                highest = upgrade
        if highest:
            highest.click()   # Click on the most expensive upgrade we can currently afford

        timeout = time.time() + 5   # Add another 5 seconds until next check for affordable upgrades

    if time.time() > five_min: # If it's been more than 5 minutes since script start, stop and check cookies per second count
        cookie_per_s = driver.find_element(by=By.ID, value="cookiesPerSecond").text  # Get current cookies per second production rate
        print(cookie_per_s)
        break  # End the bot's operation
