n,k=map(str,input().split())
nc=0
kc=0
flag=0
for i in n:
    for j in k:
        if i==k:
            flag=1 
        elif i>k:
            nc+=1
        elif i<k:
            kc+=1 
if flag==1:
    print(n)
elif nc>kc:
    print(n)
else:
    print(k)
