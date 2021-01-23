from typing import ValuesView
import jieba
fi=open('小女孩.txt','r')
txt=fi.read()
words=jieba.lcut(txt)
counts={}
fi.close()

for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,value=items[i]
    print('{0:<10}{1:>5}'.format(word,value))