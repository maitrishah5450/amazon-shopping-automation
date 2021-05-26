import requests
import bs4
import time
import csv
import re
import random
import pync
import os
import sys
from datetime import datetime

def fetch(user_agent, notifications):
    headers = {'User-Agent': user_agent}
    with open('amazon.csv', newline='') as datafile:
        data = csv.reader(datafile)
        output = ''
        with open('amazon.txt', 'a') as dataFile:
            dataFile.writelines('\n\n{:^53}\n\n'.format(datetime.now().strftime("  %d-%m-%Y %H:%M:%S  ")))
        for product in data:
            try:
                url = 'https://www.amazon.in/dp/' + product[0]
                offer_url = 'https://www.amazon.in/gp/offer-listing/' + product[0]
                req = requests.get(url, headers=headers)
                soup = bs4.BeautifulSoup(req.text, 'lxml')
                tag = soup.find(id='priceblock_ourprice')
                price = int(re.sub('[^\d.]','',tag.text)[:-3])
                buy_within = int(product[2])

                if price <= buy_within:
                    pync.notify('***STEAL DEAL***\n{} | {}'.format(product[1], price), open=url)
                    with open('amazon.txt', 'a') as dataFile:
                      dataFile.writelines('***STEAL DEAL***\n{:>40}:{:6}\n'.format(product[1], price))
                else:
                    with open('amazon.txt', 'a') as dataFile:
                      dataFile.writelines('{:>40}:{:6}{:6}\n'.format(product[1],price, buy_within))

                time.sleep(2)
            except:
                    continue


user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

if len(sys.argv) > 1:
    fetch(random.choice(user_agent_list), sys.argv[1])
else:
    fetch(random.choice(user_agent_list), '')
sys.exit()

