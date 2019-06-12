n,n1=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n1):
    k=l[len(l)-1]
    l.remove(k)
    l.insert(0,k)
for i in l:
    print(i,end=' ')
