n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if i!=len(l)-1:
        if l[i]>l[i+1]:
            print(i)
            break
