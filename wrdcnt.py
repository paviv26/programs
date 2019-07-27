l=list(map(str,input().split()))
k=input()
count=0
for i in l:
    if i==k:
        count+=1
print(count)
