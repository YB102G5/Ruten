# -*- coding: utf-8 -*-
f = open('items_detail_keywordsCode.csv', 'r')
details_dict = {}
for row in f.readlines():
    item_code = row.split(',')[1]
    details_dict[item_code] = row
f.close()
print('Details dict imported.')

f1 = open('sales_remove_repeat.csv', 'r')
content = ''
count = 0
for row in f1.readlines():
    item_code = row.split(',')[0]
    if item_code in details_dict:
        content += row.strip()
        content += ','
        content += details_dict[item_code]
    count += 1
    print(count)
f1.close()

f2 = open('combined_items_sales.csv', 'w')
f2.write(content)
f2.close()
