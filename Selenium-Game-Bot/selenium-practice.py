from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

# Set chrome to stay open after the script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initiate a driver with our options
driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
##Secondary way to get article count##
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount ul li a')
print(article_count.text)

#Find element by link
all_portals = driver.find_element(By.LINK_TEXT, value = 'Content portals')
#click element
# all_portals.click()

#find and click the search icon
search_icon = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
search_icon.click()

#Find the "search" input box
search1 = driver.find_element(By.NAME, value='search')
#type python into search
search1.send_keys('Python')
#press enter/return key
search1.send_keys(Keys.ENTER)

#close browser
driver.quit()