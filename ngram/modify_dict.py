dictFile = 'word_dict.txt'
f = open(dictFile, 'r')
content = ''
for row in f.readlines():
    list = row.split('|\t')
    content += ' '.join([''.join(list[0].strip().split()), list[1]])
f.close()

modified_dictFile = 'word_dict_modified.txt'
f = open(modified_dictFile, 'w')
f.write(content)
f.close()