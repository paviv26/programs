str=input()
count=0
for i in str:
    if i.isalpha():
        count+=1 
if count>0:
    print("no")
else:
    print("yes")
