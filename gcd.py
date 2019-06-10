n,n1=map(int,input().split())
l=list()
l1=list()
l2=list()
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in range(1,n1+1):
    if n1%i==0:
        l1.append(i)
for i in l:
    for j in l1:
        if i==j:
            l2.append(i)
print(max(l2))
