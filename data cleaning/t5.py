# check if some category not in database
f = open('items_new_catCode_new.csv', 'r')
cat_dict = {}
for row in f.readlines():
    cat1 = row.split(',')[-2]
    cat2 = row.split(',')[-1].strip()
    if cat1 == '3':
        print('in')
f.close()

#cat1 = 2 not in database.