import functools as f,collections as c,codecs as cs
with cs.open("liste_mot.txt","r",encoding="utf8") as f1,cs.open("liste_anagrammes.txt",'w+',encoding='utf8') as f2: print([el[1] or f2.write(" ".join(el[1])+"\r\n") for el in filter(lambda k:len(k[1])>1,f.reduce(lambda d,v:d.update({v[0]:d[v[0]] + [v[1]]}) or d,[("".join(sorted(el.rstrip().lower())),el.rstrip().lower()) for el in f1],c.defaultdict(list)).items())])
