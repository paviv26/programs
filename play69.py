n,n1=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n1):
    l.remove(l[len(l)-1])
print(*l)
