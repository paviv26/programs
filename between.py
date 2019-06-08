val=input()
n11,n12=map(int,input().split())
flag=0
for i in range(n11+1,n12):
    if i==val:
        flag=1 
        break
if flag==1:
    print("yes")
else:
    print("no")
