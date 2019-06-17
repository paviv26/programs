import math
n,n1=map(int,input().split())
count=0
for i in range(n+1,n1):
    if i & i-1==0:
        count+=1
print(count)
