str=input()
d={}
for n in str:
    keys=d.keys()
    if n in keys:
        d[n]+=1 
    else:
        d[n]=1
s=max(keys,key=(lambda k: d[k]))
print(s)
