l1,l2=map(str,input().split())
count=0
for i in range(len(l1)):
    if l1[i]==l2:
        count+=1
print(count)
