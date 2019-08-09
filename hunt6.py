n=int(input())
l=list(map(int,input().split()))
s=""
res=list()
for i in l:
    s=s+str(i)
for i in s:
    z=i
    cnt=s.count(z)
    if cnt>1:
        res.append(z)
        break
if len(res)==0:
    print("unique")
else:
    print(*res)
