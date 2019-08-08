n=int(input())
l=list(map(int,input().split()))
res=list()
for i in range(len(l)):
    if i==l[i]:
        res.append(l[i])
res.sort()
if len(res)==0:
    print("-1")
else:
    print(*res)
