# sales record增加category code
f = open('items_new_catCode_new.csv', 'r')
cat_dict = {}
for row in f.readlines():
    item_code = row.split(',')[1]
    cat1 = row.split(',')[-2]
    cat2 = row.split(',')[-1].strip()
    cat_dict[item_code] = [cat1, cat2]
f.close()

f1 = open('sales_remove_repeat.csv', 'r')
content = ''
count = 0
errorcount = 0
error_list = []
for row in f1.readlines():
    item_code = row.split(',')[0]
    if item_code in cat_dict:
        content += row.strip()
        content += ','
        content += ','.join(cat_dict[item_code])
        content += '\n'
    else:
        if item_code not in error_list:
            error_list.append(item_code)
            errorcount += 1
    count += 1
    print(count)
print('There are %d items which are not in item lists...'%errorcount)
f1.close()

f2 = open('sales_add_catCode.csv', 'w')
f2.write(content)
f2.close()
