n=int(input())
i=1
while n>0:
    if (n+i)%10==0:
        print(n+i)
        break
    else:
        n=n+i
