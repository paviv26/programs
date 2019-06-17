n,n1=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in l:
    if i==n1:
        flag=1
        break
if flag==1:
    print("Yes")
else:
    print("No")
