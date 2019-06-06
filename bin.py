k11=input()
count=0
for i in k11:
    if i=="1" or i=="0":
        count=count+1
if count==len(k11):
    print("yes")
else:
    print("no")
