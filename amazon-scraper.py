from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import datetime
import smtplib


anomalies = ['0%', '0% (0%', '(0%']
productTitleTags = ['title', 'productTitle']

df = pd.read_excel('C:/Users/lennovo/Desktop/lenovo.xlsx')
mylist = df['ASIN'].dropna().tolist()
print(mylist)

# asin = ['B005EJH6RW','B099HDR2Y6', 'B07YNLBS7R', 'B09B96PMLY']
url = 'https://www.amazon.com/dp/'



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
itemNameList = []
itemPriceList = []
itemAsinList = []
productLinkList = []
count=0

for i in mylist: 
    # count = count+1
    URL = url+i
    print(URL)
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    # Outer Tag Object
    title = soup2.find('title').getText().strip()
    print(title)
    # if count > 10:
    #     break
        
    price = soup2.find_all("span")
    for j in price:
        try:
            if j['class'] == ['a-offscreen']:
                count+=1

                itemPrice = f"{str(j.get_text().strip())[:-1]}"
                productLinkList.append(URL)
                itemNameList.append(title)
                itemPriceList.append(itemPrice)
                itemAsinList.append(i)
                break
                
        except KeyError:
            continue

    print(itemPrice)
    # print(ASIN_value)
    # print(price)

df1 = pd.DataFrame(list(zip(itemAsinList,itemNameList,itemPriceList,productLinkList)), columns=("ASIN","NAME","PRICE","PRODUCT LINK"))
print(df1)
df1.to_excel('OUTPUT.xlsx')
