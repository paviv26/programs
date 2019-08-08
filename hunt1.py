n=int(input())
l=list(map(int,input().split()))
d=dict()
res=[]
for i in l:
    keys=d.keys()
    if i in keys:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v>1:
        res.append(k)
res.sort()
if len(res)==0:
    print("unique")
else:
    print(*res)
