a=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l3=set(l)
l4=set(l1)
k=list()
for i in l3:
    if i in l4:
        k.append(i)
k.sort()
print(*k)    
