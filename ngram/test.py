# -*- coding: utf-8 -*-
import re
import jieba

cleanCom = r'-|=|@|～|~|─|≠|;|→|%|．|/|•|《|》|，|。|？|：|︰|！|!|／|╱|『|』|〈|〉|【|】|…|\.|——|「|」|,,|、|‧|－|）|（|；|,|\(|\)|:|—|\+|\*|「|」|☆|★|❤|＊|◎|�|●|\[|\]|✿|♥|↘|↓|_|◤'
s = '✿�抹'
m = re.search("(.*?)([a-zA-Z0-9'\.]+)(.*)", s)
# print (m.groups())

# print (bool(re.match(cleanCom, s)))

text = "回饋特價!!特級保濕免運費美國Kiehl's契爾氏冰河醣蛋白保濕霜 125ML"

seg_list = jieba.cut(text, cut_all=True)
print("Full Mode: " + ",".join(seg_list))