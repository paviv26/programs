k=input()
count=0
for i in k:
    if i.isdigit() or i.isalpha() or i==" ":
        flag=1
    else:
        count+=1
print(count)
