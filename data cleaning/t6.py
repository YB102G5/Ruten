#創造sales by month csv
from operator import itemgetter
f1 = open('sales_add_catCode.csv', 'r')
content = ''
count = 0
qty_dict = {}
for row in f1.readlines():
    item_code = row.split(',')[0]
    cat1 = row.split(',')[-2]
    cat2 = row.split(',')[-1].strip()
    qty = row.split(',')[2]
    month = '-'.join(row.split(',')[3].split('-')[0:2])
    # print(month)
    qty_dict[','.join([cat1, cat2, month])] = qty_dict.get(','.join([cat1, cat2, month]), 0)+int(qty)
    count += 1
    print(count)
f1.close()

f2 = open('sales_by_month.csv', 'w')
content = ''
for key in qty_dict:
    cat1 = key.split(',')[0]
    cat2 = key.split(',')[1]
    month = key.split(',')[2]
    qty = str(qty_dict[key])
    content += ','.join([cat1, cat2, month, qty])
    content += '\n'
f2.write(content)
f2.close()
