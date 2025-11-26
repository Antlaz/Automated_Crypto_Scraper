# automated_crypto_web_scraper.py
# Standalone version of the "Automated Crypto Web Scraper" notebook

from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/currencies/bitcoin/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

#this is the tag for the name "bitcoin" from the page. We use it in the code below.

<span data-role="coin-name" title="Bitcoin" class="sc-65e7f566-0 lsTl">Bitcoin<span class="sc-65e7f566-0 eQBACe coin-name-mobile"> price</span></span>'

#notice how we have two <spans in the above html? if we run a class_ = sc-65e7f566-0 lsTl it pulls 
#span 1 which is 'Bitcoin' and the nested span 2 which is 'price'
#So we only want to select the first span
# use.text at the end to conver the beauftiful soup to text JUST for readability tp confirm what we are grabbing
#

soup.find('span', class_ = 'sc-65e7f566-0 lsTl').text

#if we want to find just a specific tag though, which we do in this case, only the first tag bitcoin
#then we don't want it in string format. We need it in beautiful soup format, so thats what we do with this tag variable
#its the above code just minus the .text to keep it in soup format

tag = soup.find('span', class_ = 'sc-65e7f566-0 lsTl')

#selecting only the first span 'Bitcoin'
#we can use .content[] becasue this is a beautifulsoup item. It would not work if it were a string
#so, we say take the html at position [0] which is 'Bitcoin'
#and then we say .strip() to remove leading or trailing whitespace

crypto_name = tag.contents[0].strip()         # Grab ONLY the first text node (ignores 'price')
print(crypto_name)                                   # Output just 'Bitcoin'

#now we want to find the price 
#<span class="sc-65e7f566-0 WXGwg base-text" data-test="text-cdp-price-display">$87,589.68</span>
#this doesn't work becasue the webpage calls the JSON after the html, so we have to use selenium
#selenium instll below

price = soup.find('span', class_ = "sc-65e7f566-0 WXGwg")

!pip install selenium webdriver-manager

from selenium import webdriver #This gives you access to the browser automation engine. Think of webdriver like the steering wheel of the web browser.
from selenium.webdriver.chrome.service import Service #from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #This package automatically downloads the correct ChromeDriver version that matches your installed Chrome.

#we have to do this part everytime we run selenium in chrome
#just like everytime we use chrome we click the browser, thats what this does
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#this tell selenium "go to the bitcoin page"
#the browswer from the cell above MUST be open for this to work
driver.get("https://coinmarketcap.com/currencies/bitcoin/")

from selenium.webdriver.common.by import By   # brings in the "By" tool so Selenium knows HOW you want to search the page

price_tag = driver.find_element(               # tell Selenium "go find ONE element on the page"
    By.CSS_SELECTOR,                           # tell it *how* we are searching → using a CSS selector
    '[data-test="text-cdp-price-display"]'     # this is the actual selector: find the HTML element with this data-test attribute
)

price = price_tag.text                          # extract the visible text inside the span (example: "$87,644.11")
print(price)                                     # print the result so you can see the Bitcoin price in the Jupyter output

final_price = price.replace('$','')

final_price

import pandas as pd

#create a dictionary for the price info
# we have to pass a list [] because pandas expects a list in the dataframe function
date_time = datetime.now()

dict = {'Crypto Name':crypto_name,
           'Price': final_price,
            'TimeStamp': date_time}

df = pd.DataFrame([dict])

#Adding a timestamp using the datetime package

from datetime import datetime

datetime.now()

#we can fix the format by just putting a print() in there
date_time = datetime.now()

print(date_time)

#Now we export the data to a csv

df.to_csv(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv')

#now we say "if the file is already in there, we append to it, if not we create the file

import os

#so in this one we say, if the file at this path exists, then export (df.to_csv) to the file path and append the data
# ", mode = 'a' tells python to append rathern than replace
# header = False just says don't import the header from the df everytime
#the else just says "create it if it doesn't exist


if os.path.exists(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv'):
    df.to_csv(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv', mode= 'a', header = False, index = False)
else:
    df.to_csv(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv')

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os
import time
from selenium import webdriver #This gives you access to the browser automation engine. Think of webdriver like the steering wheel of the web browser.
from selenium.webdriver.chrome.service import Service #from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

def automated_crypto_pull():    
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, 'html')
    
    tag = soup.find('span', class_ = 'sc-65e7f566-0 lsTl')
    
    crypto_name = tag.contents[0].strip()         # Grab ONLY the first text node (ignores 'price')
    
    driver.get("https://coinmarketcap.com/currencies/bitcoin/")
      
    
    price_tag = driver.find_element(               # tell Selenium "go find ONE element on the page"
        By.CSS_SELECTOR,                           # tell it *how* we are searching → using a CSS selector
        '[data-test="text-cdp-price-display"]'     # this is the actual selector: find the HTML element with this data-test attribute
    )
    
    price = price_tag.text                          # extract the visible text inside the span (example: "$87,644.11")
                                  
    final_price = price.replace('$','')
    
    
    date_time = datetime.now()
    
    
    dict = {'Crypto Name':crypto_name,
               'Price': final_price,
                'TimeStamp': date_time}
    
    df = pd.DataFrame([dict])
    
    if os.path.exists(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv'):
        df.to_csv(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv', mode= 'a', header = False, index = False)
    else:
        df.to_csv(r'C:\Users\User\Desktop\Analytics\Python\Python Basics\Crypto Web Puller\Crypto_Automated_Pull.csv', index = False)
    print(df)

#this says sleep for x seconds and then run

while True:
    automated_crypto_pull()
    time.sleep(3600)
