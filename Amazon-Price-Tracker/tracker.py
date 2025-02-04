import requests  # Importing a module that allows you to send HTTP requests in Python
from bs4 import BeautifulSoup # A library used for web scraping purposes to pull the data out of HTML and XML files
import smtplib # Simple Mail Transfer Protocol client
from dotenv import load_dotenv # Loads environment variables from the .env file into your program
from email.mime.multipart import MIMEMultipart  # Used for creating multi-part MIME messages
from email.mime.text import MIMEText  # An entity that represents the body of the message
import os # This module allows you to use operating system dependent functionality

load_dotenv()   # Load environment variables from .env file

# Define global variables
URL = 'https://www.amazon.com/Crucial-16GB-Laptop-Memory-CT16G4SFRA32A/dp/B08C511GQH?th=1'  # The URL of the website we will be scraping
MAX_PRICE = 30  # Set your desired minimum price here
SMTP_EMAIL = os.getenv('SMTP_EMAIL')  # Sender's email address from `.env` file
TO_EMAIL = os.getenv('TO_EMAIL')   # Receiver's email address from `.env` file
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD') # Email password from `.env` file

#headers
headers =\
    {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,en;q=0.8,",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Opera GX\";v=\"115\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
    }

response = requests.get(url=URL, headers=headers)  # Send a GET request to the URL and store the response

soup = BeautifulSoup(response.text, 'html.parser')  # Create a BeautifulSoup object and specify the parser
price = float(soup.find(name='span', class_='a-offscreen').get_text().split('$')[1])  # Extract price from HTML using Beautiful Soup
print(f"Current price: ${price}") # Print current price to the console
def send_email():
    msg = MIMEMultipart()  # Create a message
    msg['From'] = SMTP_EMAIL  # Set sender's email address
    msg['To'] = TO_EMAIL   # Set receiver's email address
    msg['Subject'] = "Instant Pot Price Drop Alert!" # Set subject of the email

    body = f"The current price of Instant Pot is below ${MAX_PRICE}. Go check it out now: {URL}"  # Write content of the message
    msg.attach(MIMEText(body, 'plain'))   # Attach plain text version of body to email

    server = smtplib.SMTP('smtp.protonmail.ch', 587) # Set up an SMTP server with Gmail's SMTP server at port 587
    server.starttls()  # Start TLS for security
    server.login(SMTP_EMAIL, SMTP_PASSWORD)   # Log in to our email account using the app-generated password
    text = msg.as_string() # Convert message into string format
    server.sendmail(SMTP_EMAIL, TO_EMAIL, text)  # Send the mail from SMTP_EMAIL to TO_EMAIL with the content of 'text'
    server.quit()   # Log out of server
    print('Email sent!') # Print a notification that email has been successfully sent
if price < MAX_PRICE:
    send_email()  # If the price is less than minimum price, send an email using the function we created earlier.
