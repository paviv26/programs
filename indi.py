l1,l2=map(str,input().split())
for i in range(len(l1)+1):
    if l1[i]==l2:
        print(i+1)
        break
