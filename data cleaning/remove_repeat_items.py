f = open('items_modified.csv', 'r')
itemcode_list = []
content = ''
count = 0
for item in f.readlines():
    if len(item.split(',')[1]) == 14 and item.split(',')[1] not in itemcode_list:
        itemcode_list.append(item.split(',')[1])
        content += item
    count += 1
    print ('Row %d finished.'%count)
f.close()

f1 = open('items_test_1.csv', 'w')
f1.write(content)
f1.close()

print ('repeat item removed.')