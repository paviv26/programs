a,b=map(int,input().split())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i<b:
        k.append(i)
k.sort()
print(*k)
