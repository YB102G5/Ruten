# -*- coding: utf-8 -*-
import requests, time, re
from bs4 import BeautifulSoup

header = {
'Cookie':'ruten_ad_20150108-122732_expire=Tue%2C%2003%20Feb%202015%2006%3A39%3A18%20GMT; ruten_ad_20150108-122732=1; ruten_ad_20150130-164849_expire=Tue%2C%2003%20Feb%202015%2006%3A39%3A48%20GMT; ruten_ad_20150130-164849=1; _ts_id=3D04360E3C083E0D3D; _gat=1; _ga=GA1.3.1515021042.1422859158',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'}

offerLogUrl = 'http://goods.ruten.com.tw/item/history_full.php?11090823683595&page=%d#log'
n = 1

offerLog_res = requests.get(offerLogUrl%n, headers=header)
offerLog_res.encoding=('big5')
soup1 = BeautifulSoup(offerLog_res.text)
offerLog = soup1.select('.offer-log')[0]
print "page %d."%n
print offerLog
print "================================="

while len(offerLog.select('.msg')) == 0:
    for a in offerLog.select('p')[1].select('a'):
        if u"下" in a.text:
            n += 1
            offerLog_res = requests.get(offerLogUrl%n, headers=header) #下一頁網頁
            offerLog_res.encoding=('big5')
            soup1 = BeautifulSoup(offerLog_res.text)
            offerLog = soup1.select('.offer-log')[0] #取出下一頁offer log
            print "page %d."%n
            print offerLog 
            print "================================="
            break #繼續while
    else: #正常執行完for loop才會執行這個區塊?
        break #break while