# -*- coding: utf-8 -*-
import requests, time, re, os, logging, traceback, json
from bs4 import BeautifulSoup
from random import randint
from requests.exceptions import ConnectionError
from datetime import datetime

sellerId = 'beauty104'
sellURL = 'http://mybid.ruten.com.tw/credit/point?%s&sell'%sellerId
# sellURL = 'http://mybid.ruten.com.tw/credit/point?'+seller+'&sell&all&%d'

header = {
'Cookie':'_ts_id=3D0B3900360530033B; _gat=1; _ga=GA1.3.350769529.1418119264',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'}

def getTotalPageNumber(sellURL, header):
    errorcount = 0
    while True:
        try:
            res = requests.get(sellURL,headers=header)
            res.encoding=('big5')
            soup = BeautifulSoup(res.text)
            text = soup.select('.t13')[-1].text
            TotalPageNumber = int(text[text.index('/')+1:text.index(u'頁')-1])
            return TotalPageNumber
            # print 'This category has %d pages.'%page
        except Exception as e:
            errorcount += 1
            print ('Error occurred. error %d.'%errorcount)
            logging.exception(e)
            continue
        break

totalPageNum = getTotalPageNumber(sellURL, header)

# res = requests.get(sellURL,headers=header)
# res.encoding=('big5')
# soup = BeautifulSoup(res.text)
# # print (soup.findAll(text=True))
# li =  re.search('var f_list=(.*);',res.text)
#
# jele = json.loads(li.group(1))
# for ele in  jele['OrderList']: #ele為每筆評價的dict

pageurl = 'http://mybid.ruten.com.tw/credit/point?'+sellerId+'&all&all&%d'

for p in range(0, totalPageNum+1):
    res = requests.get(pageurl%p, headers=header)
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text)
    li =  re.search('var f_list=(.*);',res.text)

    jele = json.loads(li.group(1))
    for ele in  jele['OrderList']: #ele為每筆評價的dict
        if len(ele['user']) != 0: #買家有顯示
            bidurl = 'http://goods.ruten.com.tw/item/show?' + ele['no']
            res1 = requests.get(bidurl, headers=header)
            res1.encoding = 'big5'
            soup1 = BeautifulSoup(res1.text)
            dir = soup1.select('.dir')[0]
            cat = dir.select('a')[2]
            if cat.text.strip() == '臉部保養': #在此賣場買的是臉部保養的商品
                item_code = ele['no']
                title = ele['name']
                buyer = ele['user']
                bid_date_time = ele['bid_date']
                bid_date = bid_date_time.split()[0]
                bid_time = bid_date_time.split()[1]
                price = ele['money'][:-1]
                buyerpage = 'http://mybid.ruten.com.tw/credit/point?jbym&buy'


