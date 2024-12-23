import os
import requests
import time
from datetime import datetime

current_hour = datetime.now().hour
date_now = datetime.now().date()
today = f'{date_now.year}-{date_now.month}-{date_now.day}'
yesterday = f'{date_now.year}-{date_now.month}-{date_now.day-1}'
day_before_yesterday = f'{date_now.year}-{date_now.month}-{date_now.day-2}'
# print(date_now)
# print(yesterday)
# print(day_before_yesterday)

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
STOCK_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
SMS_API_KEY = os.getenv('TEXTBELT_API_KEY')

STOCK = "GME"
COMPANY_NAME = "Gamestop"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_price_and_news():
    ##GET NEWS##
    url = ('https://newsapi.org/v2/top-headlines?'
           'q=GameStop&'
           # 'country=us&'
           f'apiKey={NEWS_API_KEY}')
    news_response = requests.get(url)
    print(url)
    news_data = news_response.json()['articles'][1]
    article_title = (news_data['title'])
    article_brief = (news_data['description'])
    print(f'{article_title}\n{article_brief}')
    ##END GET NEWS##
    ##GET STOCK SYMBOL INFO##
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'
    stock_response = requests.get(url)
    stock_data = stock_response.json()

    print(stock_data['Time Series (Daily)'])
    # today_price = stock_data['Time Series (Daily)'][f'{today}']['4. close']
    yesterday_price = stock_data['Time Series (Daily)'][f'{yesterday}']['4. close']
    day_before_yesterday_price = stock_data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close']
    # print(today_price)
    print(type(yesterday_price))
    print(day_before_yesterday_price)
    if float(yesterday_price) >= float(day_before_yesterday_price) + float(day_before_yesterday_price) * .05:
        get_news()
        send_sms(f'{STOCK}: ⬆️ %5 \nHeadline: {article_title}\nSummary: {article_brief}')
    elif float(yesterday_price) <= float(day_before_yesterday_price) - float(day_before_yesterday_price) * .05:
        get_news()
        send_sms(f'{STOCK}: ⬇️ %5 \nHeadline: {article_title}\nSummary: {article_brief}')
    else:
            send_sms(f'{STOCK}: ${yesterday_price} / share \n\nHeadline: {article_title}\n\nSummary: {article_brief}')


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# Init
def get_news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'q=GameStop&'
           # 'country=us&'
           f'apiKey={NEWS_API_KEY}')
    news_response = requests.get(url)
    print(url)
    news_data = news_response.json()['articles'][1]
    article_title = (news_data['title'])
    article_brief = (news_data['description'])
    print(f'{article_title}\n{article_brief}')

# Send a seperate message with the percentage change and each article's title and description to your phone number.

def send_sms(message):
    # local_sms_server = 'http://127.0.0.1:9090/text',
    contact_1 = requests.post( 'https://textbelt.com/text',
                              {'phone': "2069541504",
                               'message': f'{message}',
                               'key': SMS_API_KEY,
                               })
    texbelt_success = contact_1.json()['success']
    textbelt_balance = contact_1.json()['quotaRemaining']
    print(f'TextBelt Success?: {texbelt_success}\nBalance Remaining: {textbelt_balance}')

def time_check():
    if current_hour == 7:
        stock_price_and_news()
    else:
        print('wait 1hr')
        time.sleep(3600)
        time_check()
time_check()


#Optional: Format the SMS message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

