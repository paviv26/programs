str=input()
n=len(str)//2
if n%2==0:
    for i in range(len(str)):
        if i==n:
            print("*",end='')
        else:
            print(str[i],end='')
else:
    for i in range(len(str)):
        if i==n or i==n-1:
            print("*",end='')
        else:
            print(str[i],end='')
