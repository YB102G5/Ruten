# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json, re

lastEndLine = 1
fileNumber = (lastEndLine/3000)*100 + 1
lineCount = (lastEndLine/3000)*3000 + 1

for filenum in range(fileNumber, 7925, 100):
    ruten_list = open('ruten/ruten_list_%d.txt'%filenum, 'r')
    for line in ruten_list.readlines():
        try:
            link = line.strip()
            m = re.match(r"([^ ]+)show\?(?P<number>.+)", link)
            filename = "%s"%(m.group('number'))
            f = open('E:/Project/ruten/items/%s.txt'%filename, 'r')
            response_text = f.read()
            # print response_text.decode('big5')
            response_text = response_text.decode('big5')
            soup = BeautifulSoup(response_text)
            f.close()

            dic = {}
            h2 = soup.select('h2')[0]
            dic["物品名稱"] = h2.text.strip()
            # print dic["物品名稱"]

            productMemo = soup.select('.product-memo')[0]
            # print productMemo

            location = productMemo.select('.location')[0]
            dic["物品所在地"] = location.select('.content')[0].text.strip()
            # print dic["物品所在地"]

            uploadTime = productMemo.select('.upload-time')[0]
            dic["上架日期"] = uploadTime.select('.date')[0].text.strip()
            # print dic["上架日期"]
            dic["上架時間"] = uploadTime.select('.time')[0].text.strip()
            # print dic["上架時間"]

            productAuctionInfo = soup.select('.product-auction-info')[0]
            # print productAuctionInfo

            soldCount = productAuctionInfo.select('.sold-count')[0]
            dic["已賣數量"] = soldCount.select('.number')[0].text.strip()
            # print dic["已賣數量"]

            ship = productAuctionInfo.select('.ship')[0]
            dic["運費"] = ship.select('.cost')[0].text.strip()
            # print dic["運費"]

            userId = productAuctionInfo.select('.user-id')[0]
            dic["賣家"] = userId.select('a')[0].text.strip()
            # print dic["賣家"]
            dic["賣場首頁"] = userId.select('a')[0]['href']
            # print dic["賣場首頁"]

            allCredit = productAuctionInfo.select('.all-credit')[0]
            dic["評價分數"] = allCredit.select('a')[0].text.strip()
            # print dic["評價分數"]

            with open('E:/Project/ruten/jsons/%s.txt'%filename, 'w') as f:
                json.dump(dic, f)
            print "json %s line %d saved."%(filename, lineCount)
            lineCount += 1
        except Exception as detail:
            print 'Error occurred when saving json %s.'%filename
            print detail