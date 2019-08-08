n=int(input())
l=list(map(int,input().split()))
k=list()
for i in range(n):
    if i!=(n-1):
        if l[i]>l[i+1]:
            k.append(l[i])
        else:
            k.append(l[i+1])
print(*k)
