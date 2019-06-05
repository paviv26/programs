n1=int(input())
hrs=0
while n1>60:
    min=n1-60
    hrs=hrs+1
    if min>60:
        n1=min
    else:
        break
if n1>60:
    print(hrs,min)
else:
    print(hrs,n1)
        
