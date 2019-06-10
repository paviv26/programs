n,n1,n3=map(str,input().split())
if n1=="%":
    res=int(n)%int(n3)
elif n1=="/":
    res=int(n)//int(n3)
print(res)
