p=int(input())
n=list(map(int,input().split()))
d={}
s=0
for i in n:
    keys=d.keys()
    if i in keys:
        d[i]+=1 
    else:
        d[i]=1 
for k,v in d.items():
    if v==1:
        print(k)
