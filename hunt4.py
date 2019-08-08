n=int(input())
l=list(map(int,input().split()))
d=dict()
for i in l:
    keys=d.keys()
    if i in keys:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v==1:
        print(k)
