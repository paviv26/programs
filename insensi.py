l3,l2=map(str,input().split())
l=l3.lower()
l1=l2.lower()
flag=0
for i in range(len(l)):
    if l[i]!=l1[i]:
        flag=1
        break
if flag==1:
    print("no")
else:
    print("yes")
