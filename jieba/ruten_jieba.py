# -*- coding: utf-8 -*-
import jieba, sys
#用jieba斷詞存成item code對keywords code的表格以及在原始的item details中加上keywords code
jieba.set_dictionary('dict_cosmetic_freq_over_100_art_adj_0326.txt.big')

f1 = open('keywords_dict_0326.csv', 'r')
cosmetic_word_dict = {}
for row in f1.readlines():
    word_code = row.split(',')[0]
    word = row.split(',')[1].strip()
    cosmetic_word_dict[word] = word_code
f1.close()


# seg_list = jieba.cut(text, cut_all=True)
# print(",".join(seg_list))  # 全模式
#
# seg_list = jieba.cut(text, cut_all=False)
# print (",".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut_for_search(text)  # 搜索引擎模式
# print(",".join(seg_list))

f = open('items_new_catCode_new.csv', 'r')
item_list = f.readlines()
f.close()
item_keywords_content = ''
# items_content = ''
count = 0
for row in item_list:
    non_repeat_filter = []
    row = row.strip()
    title = row.split(',')[0]
    item_code = row.split(',')[1].encode('utf8')
    seg_list = jieba.cut(title, cut_all=False)
    # items_content += row.strip()
    for word in seg_list:
        word = word.encode('utf8')
        if word in cosmetic_word_dict and word not in non_repeat_filter:
            non_repeat_filter.append(word)
            item_keywords_content += item_code
            item_keywords_content += ','
            item_keywords_content += str(cosmetic_word_dict[word])
            item_keywords_content += ','
            item_keywords_content += word
            item_keywords_content += '\n'
    #         items_content += ','
    #         items_content += str(cosmetic_word_dict[word])
    # items_content += '\n'
    count += 1
    print count

f2 = open('keywords_items_0330.csv', 'w')
f2.write(item_keywords_content)
f2.close()
print 'Item keywords code extracted.'

# f3 = open('items_detail_keywordsCode.csv', 'w')
# f3.write(items_content)
# f3.close()
# print 'Item keywords code appended in item details.'

