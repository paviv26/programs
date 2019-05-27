import sys
n,n1 = map(int,sys.stdin.readline().split(' '))
for i in range(n+1,n1):
    if i%2!=0:
        print(i,end=' ')
