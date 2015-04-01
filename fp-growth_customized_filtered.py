# -*- coding: utf-8 -*-
from fp_growth import find_frequent_itemsets
f = open('keywords_items_words_cat1_3_201501_201502_0327.csv', 'r')
transactions = []
count = 0
for row in f.readlines():
    counter = int(row.split(',')[-1])
    while counter > 0:
        transactions.append(row.split(',')[0:-1])
        counter -= 1
    count += 1
    print count
print 'Transactions list created.'
f.close()

f1 = open('word_dict_itemname_0326.txt')
item_dict = {}
count = 0
for row in f1.readlines():
    word = row.split()[0]
    item_dict[word] = [[], 0]
    count += 1
    print count
print 'Item names dict created.'
f1.close()

minimum_support = 100
y = find_frequent_itemsets(transactions, minimum_support)
result_dict_temp = {}
count = 0
for itemset in y:
    if len(itemset[0]) >= 3: #itemset長度起碼要三個以上
        ##############
        checker = 0
        for i in itemset[0]:
            if i in item_dict:
                checker += 1
        if checker == 1:
        #確認只有一個item在物品清單裡
        ##############
            result_dict_temp[','.join(itemset[0])] = itemset[1]
            # content += '['
            # content += ' '.join(itemset[0])
            # content += '],'
            # content += str(itemset[1])
            # content += '\n'
            # for i in itemset[0]:
            #     if i in item_dict and itemset[1] > item_dict[i][1]: #選出在item_dict裏的item而且support值更大
            #         item_dict[i] = [itemset[0], itemset[1]]
            count += 1
            print count
print 'Count: %d'%count
print 'result_dict: %d'%len(result_dict_temp)
print 'Frequent itemsets dict created.'

#過濾掉差距不大的子集合
filter_list = []
count = 0
for key1 in result_dict_temp:
    key1_list = key1.split(',')
    for key2 in result_dict_temp:
        # a
        # print count
        key2_list = key2.split(',')
        key1inkey2Checker = False
        #loop key1元素看看有沒有全在key2裏
        for i in key1_list:
            if i not in key2_list: #只要其中一個元素不在key2裏就不再看其他元素
                key1inkey2Checker = False #宣告key1不在key2裏
                # print 'key1 not in key2'
                # print count
                # count += 1
                break #換比下一個key2，下面if不會進去
            else:
                key1inkey2Checker = True
        # print key1inkey2Checker
        if key1inkey2Checker == True and len(key1) != len(key2) and (result_dict_temp[key1]-result_dict_temp[key2]) < 100 and key1 not in filter_list: #key1被key2包含而且key1值沒有大於key2 100以上，key1不要
            filter_list.append(key1)
    count += 1
    print count
print 'Count: %d'%count
print 'filter_list: %d'%len(filter_list)
print len(filter_list)

result_dict = {}
for key in result_dict_temp:
    if key not in filter_list:
        result_dict[key] = result_dict_temp[key]

content = ''
for key in result_dict:
    content += '['
    content += ' '.join(key.split(','))
    content += '],'
    content += str(result_dict[key])
    content += '\n'

f2 = open('result_cat1_3_filtered_0327.csv', 'w')
f2.write(content)
f2.close()