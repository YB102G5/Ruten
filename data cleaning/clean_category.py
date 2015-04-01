# -*- coding: utf-8 -*-
categoryFile = 'category_rm_majorCategory.csv'
cat1_dict = {}
cat2_dict = {}

def getCatDict(categoryFile):
    cf = open(categoryFile, 'r')
    for cat in cf.readlines():
        if len(cat.split(',')[2]) == 0:
            cat2 = cat.split(',')[1].strip()
            cat2No = cat.split(',')[0].strip()
            cat2_dict[cat2] = cat2No
        else:
            cat1 = cat.split(',')[2].strip()
            cat2 = cat.split(',')[1].strip()
            cat1Code = cat.split(',')[3].strip()
            cat2Code = cat.split(',')[0].strip()
            cat1_dict[cat1] = cat1Code
            cat2_dict[cat2] = cat2Code

getCatDict(categoryFile)
print(cat1_dict)
print(cat2_dict)

detailFile = 'items_test1.csv'
df = open(detailFile, 'r')
content = ''
count = 0
for item in df.readlines():
    count += 1
    # item_list = item.split(',')
    # print(item_list)
    if len(item.split(',')) == 14 and len(item.split(',')[1]) == 14: #item code為14碼且欄位為14，去除格式不對的資料
        if len(item.split(',')[13]) <= 1: #沒有大分類
            catCode = cat2_dict[item.split(',')[12]]
            cat = item.split(',')[12]
        elif item.split(',')[12] not in cat1_dict: #被刪除的大分類
            print(item.split(',')[12].strip())
            print(item.split(',')[13].strip())
            catCode = cat2_dict[item.split(',')[13].strip()]
            cat = item.split(',')[13].strip()
        else:
            catCode = cat2_dict[item.split(',')[13].strip()]+','+cat1_dict[item.split(',')[12]]
            cat = item.split(',')[13].strip()+','+item.split(',')[12]
        content += ','.join(item.split(',')[0:11])+','+catCode+','+cat+'\n'
    print(count)
df.close()

df = open('items_modified.csv', 'w')
df.write(content)
df.close()

print ('Category number created.')
