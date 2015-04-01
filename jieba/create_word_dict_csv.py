# -*- coding: utf-8 -*-
f = open('word_dict_mod1_freq_over_100_art_adj_0326.txt', 'r')
f1 = open('keywords_dict_0326.csv', 'w')
code = 1
for row in f.readlines():
    word = row.split()[0]
    f1.write(str(code))
    f1.write(',')
    f1.write(word)
    f1.write('\n')
    code += 1
f.close()
f1.close()
