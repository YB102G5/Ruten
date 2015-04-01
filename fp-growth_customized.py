# -*- coding: utf-8 -*-
#先從原本keyword_item和數量的file取出transactions，
#再取出frequent itemsets，support>100，itemset length>=3，只有一個item在item_dict裏
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

#取出frequent itemsets，support>100，itemset length>=3，只有一個item在item_dict裏
minimum_support = 100
y = find_frequent_itemsets(transactions, minimum_support)
result_dict = {}
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
            result_dict[','.join(itemset[0])] = itemset[1]
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
print 'result_dict: %d'%len(result_dict)
print 'Frequent itemsets dict created.'

content = ''
for key in result_dict:
    content += '['
    content += ' '.join(key.split(','))
    content += '],'
    content += str(result_dict[key])
    content += '\n'

f2 = open('result_cat1_3_0327.csv', 'w')
f2.write(content)
f2.close()