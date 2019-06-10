import math
n,n1=map(int,input().split())
mul=n*n1
if math.sqrt(mul)==n:
    print("yes")
else:
    print("no")
