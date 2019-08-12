l=[]
top=-1
max=100
s=''
def push(ele):
    global top
    if(top==max-1):
        print("Stack overflow")
    else:
        l.append(ele)
        top=top+1

def pop():
    global top
    global s
    if(top==-1):
        print("stack empty")
    else:
        s=s+l.pop()
        top=top-1


ch=input()
for i in ch:
    push(i)
for i in range(len(l)):
    pop()
if s==ch:
    print("YES")
else:
    print("NO")
