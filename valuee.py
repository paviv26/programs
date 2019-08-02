a,b=map(int,input().split())
l=list(map(int,input().split()))
d=dict()
for i in l:
    keys=d.keys()
    if i in keys:
        d[i]+=1
    else:
        d[i]=1
for i,j in d.items():
    if j==b:
        print(d[i])
