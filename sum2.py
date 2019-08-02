a,b=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in l:
    s=b-i
    if s in l:
        flag=1
    else:
        flag=0
if flag==0:
    print("no")
else:
    print("yes")
