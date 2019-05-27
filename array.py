import sys
n,n1 = map(int,sys.stdin.readline().split(' '))
l=list(map(int,input().split()))
sum=0
for i in range(n1):
    sum=sum+l[i]
print(sum)
