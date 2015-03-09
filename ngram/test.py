# -*- coding: utf-8 -*-
import re, os, logging, traceback, time
from datetime import datetime
from operator import itemgetter

def ngram(text, maxgram):
    if len(text) < maxgram:
        maxgram = len(text)
    dict = {}
    for gram in range(1, maxgram+1):
        for start in range(0, len(text)): #start為ngram開始點
            if (start+gram) <= len(text): #確保ngram範圍在sentence長度內
                word = text[start:start+gram] #取出ngram切出來的字
                dict[word] = dict.get(word, 0)+1
    return dict

freqDict = ngram('6瓶免運~新2017~【涵沛】蘭鑽級精粹無痕甦活霜/涵沛蘭鑽級精粹無痕甦活霜(30ml/瓶)/ 涵沛蘭鑽級甦活霜 / 蘭鑽級晶采歲月甦活霜', 5)

sortedList = sorted(freqDict.items(), key=itemgetter(1), reverse=True)

print (sortedList)

def freq2file(freqDict, file):
    #檔案不存在創檔案
    if not os.path.exists(file):
        f1 = open(file, 'w')
        f1.close()

    #讀取詞庫內容
    f = open(file, 'r')
    list = f.readlines()
    f.close()

    dict = {}
    #把詞庫內容變成dict
    if len(list) > 0: #詞庫原本有東西才做
        try:
            for row in list: #詞庫每一個詞和頻率row
                keyValueList = row.strip().split('|\t')
                key = keyValueList[0]
                value = int(keyValueList[1]) #有時詞庫詞缺頻率，因為被中斷，所以loop到那個詞會產生error
                dict[key] = value
        except IndexError as e:
            print ('Dictionary is not completed.')

    #把新的詞頻統計freqDict加進dict
    for key in freqDict:
        dict[key] = dict.get(key, 0)+freqDict[key]

    # 寫入詞庫檔案
    f2 = open(file, 'w')
    for key in dict:
        f2.write(key)
        f2.write('|\t')
        f2.write(str(dict[key]))
        f2.write('\n')
    f2.close()

# freq2file(freqDict, 'word_dict_0308_1.txt')