n=int(input())
l=list(map(str,input().split()))
l.sort(key=len)
for i in range(len(l)-1):
    if len(l[i])==len(l[i+1]) and l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(l)
