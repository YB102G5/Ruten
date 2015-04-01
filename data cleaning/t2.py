#修改變更後的category code
f = open('category_rm_majorCategory.csv', 'r')
cat1_dict = {}
cat2_dict = {}
for row in f.readlines():
    cat1 = row.split(',')[2]
    cat1_no = row.split(',')[3].strip()
    cat2 = row.split(',')[1] #有可能為空值
    cat2_no = row.split(',')[0]
    cat1_dict[cat1] = cat1_no
    if len(cat2) != 0:
        cat2_dict[cat2] = cat2_no
f.close()
print(cat1_dict)
print(cat2_dict)

f1 = open('items_mod_lotion_others_rm_repeat.csv', 'r')
content = ''
count = 0
for row in f1.readlines():
    content += ','.join(row.split(',')[0:11])
    if row.split(',')[12].strip() in cat1_dict: #第13欄為類別名稱，只有大分類
        cat1 = row.split(',')[12].strip()
        new_cat2_no = '0'
        new_cat1_no = cat1_dict[cat1]
        print(cat1)
        content += ','
        content += ','.join([new_cat1_no, new_cat2_no])
        content += '\n'
        # else:
        #     content += ','
        #     content += ','.join([new_cat1_no, new_cat2_no, cat1])
        #     content += ','
        #     content += ','.join(row.split(',')[18:])
    else: #有大小分類
        cat1 = row.split(',')[14].strip()
        print(cat1)
        cat2 = row.split(',')[13]
        print(cat2)
        new_cat1_no = cat1_dict[cat1]
        new_cat2_no = cat2_dict[cat2]
        content += ','
        content += ','.join([new_cat1_no, new_cat2_no])
        content += '\n'
        # else:
        #     content += ','
        #     content += ','.join([new_cat1_no, new_cat2_no, cat1, cat2])
        #     content += ','
        #     content += ','.join(row.split(',')[20:])
    count += 1
    print(count)
f1.close()

f2 = open('items_new_catCode.csv', 'w')
f2.write(content)
f2.close()


