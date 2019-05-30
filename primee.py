p,k=map(int,input().split())
for i in range(p+1,k):
  count=0
  for j in range(1,i+1):
    if i%j==0:
      count=count+1
  if count==2: 
      print(i)
