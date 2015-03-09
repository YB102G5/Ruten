# -*- coding: utf-8 -*-
import re, os, logging, traceback
from datetime import datetime
from operator import itemgetter
file = 'word_dict_test6.txt'
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

sortedList = sorted(dict.items(), key=itemgetter(1), reverse=True)

f2 = open(file, 'w')
for i in sortedList:
    f2.write(''.join(i[0]))
    f2.write('|\t')
    f2.write(str(i[1]))
    f2.write('\n')
f2.close()

print ('Word Dictionary sorted.')
