# -*- coding: utf-8 -*-
import re, os, logging, traceback, time
from datetime import datetime
from operator import itemgetter

cleanCom = r'-|=|@|～|~|─|≠|;|→|%|．|/|•|《|》|，|。|？|：|︰|！|!|／|╱|『|』|〈|〉|【|】|…|\.|——|「|」|,,|、|‧|－|）|（|；|,|\(|\)|:|—|\+|\*|「|」|☆|★|❤|＊|◎|�|●|\[|\]|✿|♥|↘|↓|_|◤|°|♡|\[|\]|&'

file = 'word_dict_test5.txt'
f = open(file, 'r')
list = f.readlines()
f.close()

dict = {}
#把詞庫內容變成dict
if len(list) > 0: #詞庫原本有東西才做
    try:
        for row in list: #詞庫每一個詞和頻率row
            keyValueList = row.strip().split()
            key = keyValueList[0]
            value = int(keyValueList[1]) #有時詞庫詞缺頻率，因為被中斷，所以loop到那個詞會產生error

            if len(key) > 4: #英文單字
                dict[key] = value
            elif value >= 100 and not (bool(re.match("(.*)[a-zA-Z0-9'\.~<>$]+(.*)", key)) or bool(re.match(cleanCom, key))): #頻率大於100且沒有字母符號
                dict[key] = value

    except IndexError as e:
        print ('Dictionary is not completed.')

filterList = []
count = 0
startTime = int(round(time.time() * 1000))
for key1 in dict:
    count += 1
    for key2 in dict:
        if key2 in key1 and key2 != key1 and dict[key2]/dict[key1] < 1.5: #key2是key1子字串且key2頻率不超過key1 1.5倍
            filterList.append(key2) #建立去除的filter
    print (count)
finishTime = int(round(time.time() * 1000))
period = finishTime - startTime
print ('Job duration %ds'%period)

filter_list_file = 'filter_list.txt'
f1 = open(filter_list_file, 'r')
filterList = []
for word in f1.readlines():
    filterList.append(word.strip())
f1.close()

dict2 = {}
count = 0
for key in dict:
    if not key in filterList:#沒有在filter list裡才要
        dict2[key] = dict[key]
    count += 1
    print (count)

f2 = open(file, 'w')
for key in dict2:
    f2.write(key)
    f2.write(' ')
    f2.write(str(dict2[key]))
    f2.write('\n')
f2.close()

print ('Word Dictionary cleaned.')