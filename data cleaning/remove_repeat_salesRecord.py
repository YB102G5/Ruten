f = open('sales.csv', 'r')
itemcode_datetime_list = []
content = ''
count = 0
for item in f.readlines():
    if len(item.split(',')[0]) == 14:
        key = item.split(',')[0]+item.split(',')[3]+item.split(',')[4]
        if key not in itemcode_datetime_list:
            itemcode_datetime_list.append(key)
            content += item
    count += 1
    print ('Row %d finished.'%count)
f.close()

f1 = open('sales_test_1.csv', 'w')
f1.write(content)
f1.close()

print ('repeat item removed.')