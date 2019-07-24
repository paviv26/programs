n,b=list(map(str,input().split()))
a=list(n)
p=""
for i in range(int(b)):
    if len(a)!=0:
        s=a[len(a)-1]
        del(a[len(a)-1])
        p=p+s
    else:
        break
p=p[::-1]
for i in a:
    p=p+i
print(p)
