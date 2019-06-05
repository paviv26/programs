n1=input()
flag=0
for i in n1:
    if i.isdigit() or i==".":
        flag=0
    else:
        flag=1
if flag==0:
    print("yes")
else:
    print("No")
