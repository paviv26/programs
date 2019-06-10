import math
n,n1=map(int,input().split())
mul=n*n1
if math.sqrt(mul)==n or math.sqrt(mul)==n1:
    print("yes")
else:
    print("no")
