n=int(input())
l=list(map(int,input().split()))
d=dict()
for i in l:
    keys=d.keys()
    values=d.values()
    if i in keys:
        d[i]+=1
    else:
        d[i]=1
print(max(values))
