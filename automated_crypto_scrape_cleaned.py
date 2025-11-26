from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def automated_crypto_pull():    
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, 'html')
    
    tag = soup.find('span', class_ = 'sc-65e7f566-0 lsTl')
    
    crypto_name = tag.contents[0].strip()         
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://coinmarketcap.com/currencies/bitcoin/")
      
    price_tag = driver.find_element(             
        By.CSS_SELECTOR,                          
        '[data-test="text-cdp-price-display"]'     
    )
    
    price = price_tag.text                        
                                  
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

while True:
    automated_crypto_pull()
    time.sleep(3600)
