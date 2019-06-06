k11=input()
cd=0
ca=0
for i in k11:
    if i.isdigit():
        cd=cd+1 
    elif i.isalpha():
        ca+=1 
if ca>1 and cd>1:
    print("Yes")
else:
    print("No")
