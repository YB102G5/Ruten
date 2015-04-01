from operator import itemgetter
f1 = open('sales_add_catCode.csv', 'r')
content = ''
count = 0
qty_dict = {}
for row in f1.readlines():
    month = '-'.join(row.split(',')[3].split('-')[0:2])
    # print(month)
    if month in ['2015-01', '2015-02']:
        item_code = row.split(',')[0]
        # cat1_code = row.split(',')[-2]
        # cat2_code = row.split(',')[-1].strip()
        qty = row.split(',')[2]
        qty_dict[item_code] = qty_dict.get(item_code, 0)+int(qty)
    count += 1
    print(count)
f1.close()

f2 = open('items_new_catCode_new.csv', 'r')
content = ''
for row in f2.readlines():
    row = row.strip()
    content += row
    item_code = row.split(',')[1]
    if item_code in qty_dict:
        content += ','
        content += str(qty_dict[item_code])
        content += '\n'
    else:
        content += ','
        content += '0'
        content += '\n'
f2.close()

f3 = open('items_new_catCode_new_qty_201501_201502.csv', 'w')
f3.write(content)
f3.close()
