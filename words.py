import jieba
fi=open ('小女孩.txt','r')
fo=open('排序.txt','w')
text=fi.read()
fi.close()
counts={}
exclude='，。/《》？；‘’；“”：【】、！'
words= jieba.lcut(text)
for word in words:
    if len(word)==1 or word in exclude:
        continue
    else:
        counts[word]=counts.get(word,0)+1

ls=list(counts.items())
ls.sort(key=lambda x:x[1],reverse=True)

for i in range(len(ls)):
    word,value=ls[i]
    ls[i]='{}:{}'.format(word,value)
    print('{0:<5}{1:>10}'.format(word,value))

fo.write(','.join(ls))    
fo.close()


