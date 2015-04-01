from operator import itemgetter

f = open('combined_items_sales_mod_catCode.csv', 'r')
dict = {}
qty_dict = {}
count = 0
for record in f.readlines():
    item_code = record.split(',')[0]
    cat1_code = record.split(',')[16]
    cat2_code = record.split(',')[17].strip()
    qty_dict[item_code] = qty_dict.get(item_code, 0)+int(record.split(',')[2])
    dict[item_code] = {'cat1_code':cat1_code, 'cat2_code':cat2_code, 'qty':str(qty_dict[item_code])}
    count += 1
    print(count)
f.close()

f1 = open('keywords_items.csv', 'r')
content = ''
count = 0
for row in f1.readlines():
    item_code = row.split(',')[0]
    if item_code in dict:
        content += row.strip()
        cat1_code = dict[item_code]['cat1_code']
        cat2_code = dict[item_code]['cat2_code']
        qty = dict[item_code]['qty']
        content += ','
        content += ','.join([cat1_code, cat2_code, qty])
        content += '\n'
    count += 1
    print(count)
f1.close()

f2 = open('items_keywords.csv', 'w')
f2.write(content)
f2.close()
