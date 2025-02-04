# Import required libraries
from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import datetime

# Set chrome to stay open after the script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initiate a driver with our options
driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://python.org/')


#####WALKTHROUGH SOLUTION TO FINDING AND SPLITTING THE EVENTS WIDGET DATA#####
events = {}

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
for time in event_times:
    current_year = str(datetime.date.today().year)
    full_date = current_year + '-' + time.text
    print(full_date)

event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
for name in event_names:
    print(name.text)

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text,
    }
print(events)
#####END WALKTHROUGH#####

#####MY SOLUTION TO FINDING AND SPLITTING THE EVENTS WIDGET DATA######
# upcoming_events_menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
# # print(upcoming_events_menu)
#
#
# # Split the text based on new lines.
# events_list = upcoming_events_menu.strip().split('\n')
#
# # Create an empty list to store events and dates.
# event_dict = []
# for i in range(0, len(events_list), 2):
#     date = events_list[i].strip()
#     event = events_list[i+1].strip()
#     # Add the date-event pair to the dictionary.
#     event_dict.append({'index': i//2, 'time': date, 'name': event})
#
# print(event_dict)

driver.quit()


# # Locate the search bar on Python.org page by its name attribute and print it
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar)
#
# # Locate the submit button on Python.org page by its id attribute and print it
# button = driver.find_element(By.ID, value='submit')
# print(button)
#
# # Locate the documentation link on Python.org page by its CSS selector and print its text
# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(documentation_link.text)
#
# # Locate the bug report link on Python.org page by its XPath and print its text
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


####AMAZON PRICE BOT##################################################################################################
# def get_price():
#     try:
#         # Find and get the text of the dollar portion of price
#         price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
#
#         # Find and get the text of the cent portion of price
#         price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text
#     except (NoSuchElementException, ElementNotInteractableException) as e:
#         return None
#
#     # Return the final price
#     return f'The price is: ${price_dollar}.{price_cents}'
#
# while True:
#     try:
#         # Attempt to get the page
#         driver.get(url='https://www.amazon.com/Crucial-16GB-Laptop-Memory-CT16G4SFRA32A/dp/B08C511GQH?th=1')
#     except Exception as e:
#         # If an error occurs, print the error message and continue the loop
#         print('An error occurred while trying to access the page:', str(e))
#         continue
#
#     price = get_price()
#
#     if price is not None:
#         print(price)
#         driver.quit()
#         break