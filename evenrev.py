n11=int(input())
str=input()
l=list()
vow=['a','e','i','o','u','A','E','I','O','U']
for i in str:
    if i not in vow:
        l.append(i)
l1=l[::-1]
for i in l1:
    print(i,end='')
