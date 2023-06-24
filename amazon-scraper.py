from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

URL = 'https://www.amazon.com/dp/B005EJH6RW'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# print(soup1.prettify().encode("utf-8"))

ASIN = soup2.find(id='ASIN')

# price = soup2.find(id='priceblock_ourprice')


price = soup2.find_all("span")
for i in price:
    try:
        if i['class'] == ['a-price-whole']:
            itemPrice = f"${str(i.get_text().strip())[:-1]}"
            break
    except KeyError:
        continue

print(itemPrice)
# print(ASIN_value)
# print(price)