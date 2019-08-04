n=int(input())
l=list(map(int,input().split()))
k=dict()
for i in range(len(l)):
    if i==0:
        key=l[i]
        k[key]=1
    else:
        current=l[i]
        if current==key:
            k[key]=k[key]+1
            key=current
        else:
            key=current
            k[key]=1
    
s=k.values()
print(max(s))
