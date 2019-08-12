l=list(map(str,input().split()))
res=[]
for i in l:
    res.append(i[::-1])
print(*res)
