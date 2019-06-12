str1=input()
for i in range(len(str1)):
    if i%2==0:
        print(str1[i+1],end='')
    else:
        print(str1[i-1],end='')
