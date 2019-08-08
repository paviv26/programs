n,n1=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
flag=0
for i in l1:
    if i not in l:
        flag=1
if flag==1:
    print("NO")
else:
    print("YES")
