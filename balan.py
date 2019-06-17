str=input()
count=0
count1=0
for n in str:
    if n=='(':
        count+=1
    elif n==')':
        count1+=1
if count==count1:
    print('yes')
else:
    print("no")
