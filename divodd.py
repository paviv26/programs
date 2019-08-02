a=int(input())
for i in range(1,a):
    div=a//i
    if div%2!=0:
        print(i)
        break
