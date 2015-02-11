# -*- coding: utf-8 -*-
import requests, time, re
from bs4 import BeautifulSoup
from random import randint

header = {
'Cookie':'ruten_ad_20150108-122732_expire=Tue%2C%2003%20Feb%202015%2006%3A39%3A18%20GMT; ruten_ad_20150108-122732=1; ruten_ad_20150130-164849_expire=Tue%2C%2003%20Feb%202015%2006%3A39%3A48%20GMT; ruten_ad_20150130-164849=1; _ts_id=3D04360E3C083E0D3D; _gat=1; _ga=GA1.3.1515021042.1422859158',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'}

lastEndLine = 3076
fileNumber = (lastEndLine/3000)*100 + 1
lineCount = (lastEndLine/3000)*3000 + 1
print "startPageNumber starts from %d, lineCount starts from %d."%(fileNumber, lineCount)

for filenum in range(fileNumber, 7925, 100):
    ruten_list = open('ruten/0206-0209/ruten_list_%d.txt'%filenum, 'r') #打開商品網址list檔案
    for line in ruten_list.readlines():
        errorcount = 0
        while True:
            try:
                link = line.strip()
                m = re.match(r"([^ ]+)show\?(?P<number>.+)", link) 
                filename = "%s"%(m.group('number'))
                #print filename
                request_get = requests.get(link, headers=header) 
                request_get.encoding=('big5')
                soup = BeautifulSoup(request_get.text)
                #print soup.select('#printArea')
                printarea = soup.select('.auction-data')[0]
                item_detail = open("/Users/shu-hsienchiu/PycharmProjects/pythonetl/ruten/item_offerDetail/%s.txt"%(filename), 'w')
                #print printarea
                item_detail.write(printarea.prettify("big5") + "\n")

                #取出價記錄
                offerLogUrl = 'http://goods.ruten.com.tw/item/history_full.php?'+filename+'&page=%d#log' #如何代換其中一個%為已知另一個%維持未知？
                n = 1

                offerLog_res = requests.get(offerLogUrl%n, headers=header)
                offerLog_res.encoding=('big5')
                soup1 = BeautifulSoup(offerLog_res.text)
                offerLog = soup1.select('.offer-log')[0]
                # print "page %d."%n
                # print offerLog
                # print "================================="
                item_detail.write(offerLog.prettify("big5") + "\n")

                while len(offerLog.select('.msg')) == 0:
                    for a in offerLog.select('p')[1].select('a'):
                        if u"下" in a.text:
                            n += 1
                            offerLog_res = requests.get(offerLogUrl%n, headers=header) #下一頁網頁
                            offerLog_res.encoding=('big5')
                            soup1 = BeautifulSoup(offerLog_res.text)
                            offerLog = soup1.select('.offer-log')[0] #取出下一頁offer log
                            # print "page %d."%n
                            # print offerLog
                            # print "================================="
                            item_detail.write(offerLog.prettify("big5") + "\n")
                            break #繼續while
                    else: #正常執行完for loop才會執行這個區塊?
                        break #break while

                item_detail.close()

                print "file %s line %d saved"%(filename, lineCount)
                lineCount = lineCount + 1
            except IndexError as detail:
                errorcount += 1
                print 'This auction file %s has been ended.'%filename
                print detail
                break
            except Exception as detail:
                errorcount += 1
                print 'Error occurred when capturing file %s line %d. error %d.'%(filename, lineCount, errorcount)
                print detail
                continue
            break
        time.sleep(randint(1,10)*0.1)
    ruten_list.close()
print "Job done!"