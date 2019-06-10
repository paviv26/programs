str=input()
flag=0
dict={}
for n in str:
   keys=dict.keys()
   if n in keys:
       dict[n]=dict[n]+1 
   else:
        dict[n]=1
for k,v in dict.items():
    if (v>1):    
      flag=1
if flag==1:
    print("No")
else:
    print("Yes")
