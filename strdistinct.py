s=input()
n=len(s)
l=list()
l1=list()
for i in range(n): 
    for g in range(i+1,n+1): 
        d={}
        flag=0
        z=s[i: g]
        for j in z:
            keys=d.keys()
            if j in keys:
                d[j]+=1 
            else:
                d[j]=1 
        for k,v in d.items():
            if v>1:
                flag=1 
        if flag==0:
            l.append(z)
for i in l:
    l1.append(len(i))
print(max(l1))
