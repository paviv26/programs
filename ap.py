n,a,d=map(int,input().split())
l=list()
for i in range(n):
    if i==0:
        l.append(a)
    else:
        t=a+d 
        l.append(t)
        a=t
    
print(sum(l))
