str,str1=map(str,input().split())
count=0
for i in range(len(str)):
    if str[i]!=str1[i]:
        count+=1 
if count==1:
    print("yes")
else:
    print('no')
