# -*- coding: utf-8 -*-
categoryFile = 'category_no_repeat.csv'

def getCatDict(categoryFile):
    cf = open(categoryFile, 'r')
    cat_dict = {}
    for cat in cf.readlines():
        cat1 = cat.split(',')[2].strip()
        cat2 = cat.split(',')[1].strip()
        catNo = int(cat.split(',')[0].strip())
        if len(cat1) == 0:
            catAll = cat2
        else:
            catAll = cat1+'|'+cat2
        cat_dict[catAll] = catNo
    return cat_dict

detailFile = 'items.csv'
df = open(detailFile, 'r')
content = ''
cat_dict = getCatDict(categoryFile)
for item in df.readlines()[1:]:
    if len(item.split(',')) == 14:
        if len(item.split(',')[13]) < 2:
            catAll = item.split(',')[12].strip()
        else:
            catAll = item.split(',')[12]+'|'+item.split(',')[13].strip()
        content += ','.join(item.split(',')[0:11])+','+str(cat_dict[catAll])+'\n'
df.close()

df = open(detailFile, 'w')
df.write(content)
df.close()

print ('Category number created.')
