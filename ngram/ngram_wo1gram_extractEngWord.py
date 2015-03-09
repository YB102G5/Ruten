# -*- coding: utf-8 -*-
import re, os, logging, traceback, time
from datetime import datetime
from operator import itemgetter

def list2freqdict(mylist):
        mydict=dict()
        for ch in mylist:
            mydict[ch]=mydict.get(ch,0)+1
        return mydict

def list2bigram(mylist):
        return [mylist[i:i+2] for i in range(0,len(mylist)-1)]

def list2trigram(mylist):
    return [mylist[i:i+3] for i in range(0,len(mylist)-2)]

def list2quadgram(mylist):
    return [mylist[i:i+4] for i in range(0,len(mylist)-3)]

def bigram2freqdict(mybigram):
    mydict=dict()
    for (ch1,ch2) in mybigram:
        mydict[(ch1,ch2)]=mydict.get((ch1,ch2),0)+1
    return mydict

def trigram2freqdict(mytrigram):
    mydict=dict()
    for (ch1,ch2,ch3) in mytrigram:
        mydict[(ch1,ch2,ch3)]=mydict.get((ch1,ch2,ch3),0)+1
    return mydict

def quadgram2freqdict(myquadgram):
    mydict=dict()
    for (ch1,ch2,ch3,ch4) in myquadgram:
        mydict[(ch1,ch2,ch3,ch4)]=mydict.get((ch1,ch2,ch3,ch4),0)+1
    return mydict

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
                if len(key) == 1:
                    dict[key] = value
                if len(key) > 1:
                    keyTuple = ()
                    for ch in key:
                        keyTuple = keyTuple + (ch,)
                    dict[keyTuple] = value
        except IndexError as e:
            print ('Dictionary is not completed.')

    word_tuple = ()
    for ch in word:
        word_tuple = word_tuple + (ch,)

    #把dict同樣的word次數加一
    dict[word_tuple] = dict.get(word_tuple, 0)+1

    # 寫入詞庫檔案
    f2 = open(file, 'w')
    chs=str()
    for key in dict:
        for ch in key:
            chs=chs+ch
        f2.write(chs)
        f2.write('|\t')
        f2.write(str(dict[key]))
        f2.write('\n')
        chs=''
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

def append_word_base(text, file): #做斷詞、統計頻率和寫入詞庫檔案
    segmentList = text.split()
    for segment in segmentList:

        if bool(re.match("^[a-zA-Z'\.]+$", segment)):
            engWord2file(segment, file)

        if len(segment) >= 4:
            chlist=[ch for ch in segment]
            # chfreqdict=list2freqdict(chlist) #建立次數統計字典，一個字不用tuple

            # chfreqsorted=sorted(chfreqdict.items(), key=itemgetter(1), reverse=True) #統計後的字典元素照出現頻率排序
            #
            # chfreqsorted2=chfreqsorted[:5] #取頻率最高前五名
            #
            # chfreqsorted3=list() #限定出現次數大於某數字
            # for (ch,num) in chfreqsorted:
            #     if num > 1:
            #         chfreqsorted3.append((ch,num))

            #創造2-4gram list
            chbigram=list2bigram(chlist)
            chtrigram=list2trigram(chlist)
            chquadgram=list2quadgram(chlist)
            # print(chbigram)
            # print(chtrigram)
            # print (chquadgram)

            #2-4gram list次數頻率統計，未排序
            bigramfreqdict=bigram2freqdict(chbigram)
            trigramfreqdict=trigram2freqdict(chtrigram)
            quadgramfreqdict=quadgram2freqdict(chquadgram)
            # print(bigramfreqdict)
            # print(trigramfreqdict)
            # print (quadgramfreqdict)

            #頻率統計list排序，結果為tuple list，不是dict
            # bigramfreqsorted=sorted(bigramfreqdict.items(), key=itemgetter(1), reverse=True)
            # trigramfreqsorted=sorted(trigramfreqdict.items(), key=itemgetter(1), reverse=True)
            # quadgramfreqsorted=sorted(quadgramfreqdict.items(), key=itemgetter(1), reverse=True)
            # print(bigramfreqsorted[:5])
            # print(trigramfreqsorted[:5])
            # print(quadgramfreqsorted)

            #把頻率統計dict加入詞庫
            # freq2file(chfreqdict, file)
            freq2file(bigramfreqdict, file)
            freq2file(trigramfreqdict, file)
            freq2file(quadgramfreqdict, file)

        if len(segment) == 3:
            chlist=[ch for ch in segment]
            # chfreqdict=list2freqdict(chlist) #建立次數統計字典，一個字不用tuple
            chbigram=list2bigram(chlist)
            chtrigram=list2trigram(chlist)

            bigramfreqdict=bigram2freqdict(chbigram)
            trigramfreqdict=trigram2freqdict(chtrigram)

            # freq2file(chfreqdict, file)
            freq2file(bigramfreqdict, file)
            freq2file(trigramfreqdict, file)

        if len(segment) == 2:
            chlist=[ch for ch in segment]
            # chfreqdict=list2freqdict(chlist) #建立次數統計字典，一個字不用tuple
            chbigram=list2bigram(chlist)

            bigramfreqdict=bigram2freqdict(chbigram)

            # freq2file(chfreqdict, file)
            freq2file(bigramfreqdict, file)

        # if len(segment) == 1:
        #     chlist=[ch for ch in segment]
        #     chfreqdict=list2freqdict(chlist) #建立次數統計字典，一個字不用tuple
        #     freq2file(chfreqdict, file)

#####################################################################################################################

f = open('items_page_1_11.csv', 'r')
list = f.readlines()
f.close()
rowCount = 1
wordDictFile = 'word_dict_test2.txt'
startTime = int(round(time.time() * 1000))
for row in list[1:]: #商品內容表格row
    try:
        title = row.split(',')[0]
        append_word_base(title, wordDictFile) #每個商品都要把詞庫打開建立詞庫dict再把斷詞詞頻加入
        print ('Append word base from row %d.'%rowCount)

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
