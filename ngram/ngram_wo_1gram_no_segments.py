# -*- coding: utf-8 -*-
import re, os, logging, traceback, time
from datetime import datetime
from operator import itemgetter

cleanCom = r'-|=|@|～|~|─|≠|;|→|%|．|/|•|《|》|，|。|？|：|︰|！|!|／|╱|『|』|〈|〉|【|】|…|\.|——|「|」|,,|、|‧|－|）|（|；|,|\(|\)|:|—|\+|\*|「|」|☆|★|❤|＊'

def ngram_wo_1gram(text, maxgram):
    if len(text) < maxgram:
        maxgram = len(text)
    dict = {}
    for gram in range(2, maxgram+1):
        for start in range(0, len(text)): #start為ngram開始點
            if (start+gram) <= len(text): #確保ngram範圍在sentence長度內
                word = text[start:start+gram] #取出ngram切出來的字
                dict[word] = dict.get(word, 0)+1
    return dict

def engWord2file(word, file):
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

    #把dict同樣的word次數加一
    dict[word] = dict.get(word, 0)+1

    # 寫入詞庫檔案
    f2 = open(file, 'w')
    for key in dict:
        f2.write(key)
        f2.write('|\t')
        f2.write(str(dict[key]))
        f2.write('\n')
    f2.close()

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
    #叫一次freq2file func就要做兩次IO

def append_word_dict(text, file): #做斷詞、統計頻率和寫入詞庫檔案
        freqDict = ngram_wo_1gram(text, 4)
        freq2file(freqDict, file)

#####################################################################################################################
sourceFile = 'items_test.csv'
f = open(sourceFile, 'r')
list = f.readlines()
f.close()
rowCount = 1
wordDictFile = 'word_dict_test3.txt'
startTime = int(round(time.time() * 1000))
for row in list: #商品內容表格row
    try:
        title = row.split(',')[0]
        append_word_dict(title, wordDictFile) #每個商品都要把詞庫打開建立詞庫dict再把斷詞詞頻加入
        print ('Append word dictionary from row %d.'%rowCount)

    except Exception as e:
        print ('Error occurred when dealing with row %d.'%(rowCount))
        logging.exception(e)

        #存error log
        error_file_dir = 'error/'
        if not os.path.exists(error_file_dir):
            os.makedirs(error_file_dir)
        error_file = open(error_file_dir + '%d.txt'%(rowCount), 'w')
        error_file.write('Error occurred when dealing with row %d.'%(rowCount+1))
        error_file.write('\n')
        error_file.write(str(datetime.now()))
        error_file.write('\n')
        error_file.write(traceback.format_exc())
        error_file.close()
        print ('Error log saved.')
    rowCount += 1
finishTime = int(round(time.time() * 1000))
period = finishTime - startTime
print ('Job duration %ds'%period)
