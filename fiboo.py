n=int(input())
a=1
a1=1
for i in range(1,n+1):
    if i==1 or i==2:
        print(a,end=' ')
    else:
        temp=a+a1
        print(temp,end=' ')
        a=a1
        a1=temp
