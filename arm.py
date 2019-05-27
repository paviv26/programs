n=int(input())
sum=0
n1=n
while n>0:
    temp=n%10
    sum=sum+temp*temp*temp
    n=n//10
if sum==n1:
   print("yes")
else:
   print("no")
