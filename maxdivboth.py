n,n1=map(int,input().split())
k=min(n,n1)
l=list()
for i in range(1,k+1):
    if n%i==0 and n1%i==0:
        l.append(i)
print(max(l))
