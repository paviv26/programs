p,k=map(int,input().split())
l=list()
for i in range(p,k+1):
  count=0
  for j in range(1,i+1):
    if i%j==0:
      count=count+1
  if count==2: 
      l.append(i)
print(len(l))
