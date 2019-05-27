import sys
n1,n2 = map(int,sys.stdin.readline().split(' '))
for i in range(n1+1,n2):
  count=0
  for j in range(1,i+1):
    if i%j==0:
      count=count+1
  if count==2: 
      print(i,end=' ')
