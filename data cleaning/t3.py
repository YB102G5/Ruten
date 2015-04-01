# items csv加上真正銷售量及銷售時間區間
from datetime import date
f = open('sales_remove_repeat.csv', 'r')
qty_dict = {}
count = 0
content = ''
for record in f.readlines():
    item_code = record.split(',')[0]
    qty_dict[item_code] = qty_dict.get(item_code, 0)+int(record.split(',')[2])
    count += 1
    print(count)
f.close()

count = 0
f1 = open('items_new_catCode.csv', 'r')
for record in f1.readlines():
    item_code = record.split(',')[1]
    if item_code in qty_dict:
        content += ','.join(record.split(',')[0:5])
        open_date =  record.split(',')[3]
        year= int(open_date.split('-')[0])
        month = int(open_date.split('-')[1])
        day = int(open_date.split('-')[2])
        open_date = date(year, month, day)
        if open_date < date(2013, 2, 27):
            open_date = date(2013, 2, 27)
        end_date = date(2015, 3, 4)
        diff = end_date - open_date
        period = str(diff.days)
        content += (','+period)
        content += (','+','.join(record.split(',')[5:7]))
        qty = str(qty_dict[item_code])
        content += (','+qty)
        content += ','
        content += ','.join(record.split(',')[7:])
    count += 1
    print(count)
f1.close()

f2 = open('items_new_catCode_new.csv', 'w')
f2.write(content)
f2.close()