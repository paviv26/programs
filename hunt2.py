n=int(input())
l=list(map(int,input().split()))
s=""
l.sort(reverse=True)
for i in l:
    s=s+str(i)
print(int(s))
