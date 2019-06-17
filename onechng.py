n,a,b=map(str,input().split())
count=0
p=0
for i in n:
    if i!=a[p]:
        count+=1
    p+=1
if count==int(b):
    print("yes")
else:
    print("no")
