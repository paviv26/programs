p,q=map(int,input().split())
r,s=map(int,input().split())
t,u=map(int,input().split())
if p==q and r==s and t==u:
    print("yes")
elif p==r==t or q==s==u:
    print("yes")
else:
    print("no")
