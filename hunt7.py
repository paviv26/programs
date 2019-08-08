n=int(input())
l=list(map(int,input().split()))
res=list()
for i in range(len(l)):
    if i%2==0 and l[i]%2!=0:
        res.append(l[i])
    elif i%2!=0 and l[i]%2==0:
        res.append(l[i])
print(*res)
