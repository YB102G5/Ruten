# -*- coding: utf-8 -*-
import re, time
doc_dic = {}
sen_dic = {}
words_dic = {}
cleanNum = r'\d+'
cleanCom = r'-|=|@|～|─|≠|;|→|%|．|/|•|《|》|，|。|？|：|︰|！|!|／|╱|『|』|〈|〉|【|】|…|\.|——|「|」|,,|、|‧|－|）|（|；|,|\(|\)|:|—| +'
findEng = r'[a-zA-Z]+'


def ngram(dic, gram): #把sentence字典丟進去產生words統計頻率的字典
    for sentence in dic: #sentence dic
        for start in range(0,  len(sentence.decode('utf-8'))): #start為ngram開始點
            if (start+gram) <= len(sentence.decode('utf-8')): #確保ngram範圍在sentence長度內
                words = sentence.decode('utf-8')[start:start+gram] #取出ngram切出來的字
                if words not in words_dic:
                    words_dic[words] = 1
                else:
                    words_dic[words] += 1
    return words_dic

def cutsentence(doc_dic, gram):
    sen_dic.clear()
    words_dic.clear()
    for content in doc_dic: #新聞line
        content = content.decode('utf8').strip()
        #text = re.sub(cleanNum, '', content).encode('utf-8')
        text = re.sub(r'\w+', '', content).encode('utf-8')
        text_clean = re.sub(cleanCom, '|', text) 
        newscon = text_clean.split('|')
        for putSentence in newscon:
            if putSentence not in '':
                sen_dic[putSentence] = ''
    words_list = ngram(sen_dic, gram)
    return words_list

def clean(path, gram):
    doc_dic.clear()
    sen_dic.clear()
    words_dic.clear()
    f = open(path, 'r')
    for line in f.readlines():
        line = line.replace(' ','').replace('　','')
        doc_dic[line] = '' #line設定為key, value為null字串
    words_list = cutsentence(doc_dic, gram)
    words_list_sort = sorted(words_list.iteritems(), key=lambda d:d[1], reverse = True)
    #f = open("5gram_11month_output.txt",'w')

    for ngram_output in words_list_sort:
        if ngram_output[1] >= 10 :
            f1.write(ngram_output[0].encode('utf8').strip()+" "+ str(ngram_output[1])+' '+'\n')
    #f.close()
    return words_list_sort
t1 = time.time()
print t1
f1 = open("news_ngram.txt",'w')
for gram in range(2,6):
    clean('news.txt',gram)
f1.close()
t2 = time.time()
print t2-t1