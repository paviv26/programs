n=input()
l=list()
l1=list()
for i in range(len(n)):
    if i%2==0:
        l.append(n[i])
    else:
        l1.append(n[i])
for i in range(len(l)):
    if i!=len(l)-1:
        print(l[i],end='')
    else:
        print(l[i],end=' ')
for i in l1:
    print(i,end='')
