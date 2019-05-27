import sys
a,b = map(int,sys.stdin.readline().split(' '))
l=list()
for i in range(a,b):
    sum=0
    n1=i
    while i>0:
        temp=i%10
        sum=sum+temp*temp*temp
        i=i//10
    if sum==n1:
       l.append(n1)
for i in l:
    print(i,end=' ')
