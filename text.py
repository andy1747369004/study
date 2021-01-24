import jieba
fi=open('小女孩.txt','r')
text=fi.read()
words=jieba.lcut(text)
fi.close()
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(len(items)):
    word,value=items[i]
    print("{0:<10}:{1:>5}".format(word,value))
