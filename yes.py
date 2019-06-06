n1,n2=map(int,input().split())
n=list(map(int,input().split()))
count=0
for i in n:
    if i==n2:
        count+=1 
if count>1:
    print("Yes")
else:
    print("No")
