seg_list = jieba.cut("berji 槴子花柔嫩皙白化妝水135ml 嫩白化妝水 保濕噴霧 另有槴子花身體乳液", cut_all=True)
print("Full Mode: " + ",".join(seg_list))  # 全模式

seg_list = jieba.cut("berji 槴子花柔嫩皙白化妝水135ml 嫩白化妝水 保濕噴霧 另有槴子花身體乳液", cut_all=False)
print("Default Mode: " + ",".join(seg_list))  # 精确模式

seg_list = jieba.cut("berji 槴子花柔嫩皙白化妝水135ml 嫩白化妝水 保濕噴霧 另有槴子花身體乳液")  # 默认是精确模式
print(",".join(seg_list))

seg_list = jieba.cut_for_search("berji 槴子花柔嫩皙白化妝水135ml 嫩白化妝水 保濕噴霧 另有槴子花身體乳液")  # 搜索引擎模式
print(",".join(seg_list))

from __future__ import print_function
import sys
sys.path.append("../")
jieba.load_userdict("userdict.txt") #自定义词典的路径

test_sent = "berji 槴子花柔嫩皙白化妝水135ml 嫩白化妝水 保濕噴霧 另有槴子花身體乳液"
test_sent += "[限量超低價] Uriage優麗雅含氧等滲透壓活泉噴霧300ml"
words = jieba.cut(test_sent)

print(",".join(words))

text = "berji 槴子花柔嫩皙白化妝水135ml 嫩白化妝水 保濕噴霧 另有槴子花身體乳液"
#TOP 1 字詞
tags = jieba.analyse.extract_tags(text,2)
print (",".join(tags))


# In[100]:


content = open('lyric.txt', 'rb').read()

print ("Input：", content)
#TOP 10 字詞
tags = jieba.analyse.extract_tags(content, 10)

print ("Output：")
print (",".join(tags))


# In[90]:


content = open('lyric.txt', 'rb').read()

print ("Input：", content)

words = jieba.cut(content, cut_all=False)

print ("Output 精確模式 Full Mode：")
for word in words:
    print (word)


# In[ ]:



