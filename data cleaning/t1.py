# -*- coding: utf-8 -*-
#把"乳液->其他"改成一個分類"其他乳液"
detailFile = 'items.csv'
df = open(detailFile, 'r')
content = ''
for item in df.readlines():
    if len(item.split(',')) == 14:
        if item.split(',')[12] == '乳液' and item.split(',')[13].strip() == '其他':
            print('v')
            content += ','.join(item.split(',')[0:13])+',其他乳液\n'
            continue
        content += item
df.close()
f = open('items_test1.csv', 'w')
f.write(content)
f.close()