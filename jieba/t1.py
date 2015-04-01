#取出包含特定關鍵詞item_code給R做迴歸測試
# -*- coding: utf-8 -*-
f = open('items_new_catCode_new.csv', 'r')
count = 0
keywords_list = ['面膜', '淨白', '無瑕']
item_code_list = []
for row in f.readlines():
    title = row.split(',')[0]
    qty = row.split(',')[8]
    price = row.split(',')[6]
    checker = 0
    for i in keywords_list:
        if i in title:
            checker += 1
    if checker == len(keywords_list):
        count += 1
        item_code = row.split(',')[1]
        item_code_list.append(item_code)
        print(title, price, qty)
f.close()
print(count)


f1 = open('regression_test_item_2.csv', 'w')
for i in item_code_list:
    f1.write(i)
    f1.write('\n')
f1.close()