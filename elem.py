n,n1=map(int,input().split())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i%2!=0:
        k.append(i)
for i in range(1,len(k)+1):
    if i==n1:
        print(k[i-1])
