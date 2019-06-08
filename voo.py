atr=input()
flag=0
vow=['a','e','i','o','u','A','E','I','O','U']
for i in atr:
    if i in vow:
        flag=1 
if flag==1:
    print("yes")
else:
    print("no")
    
