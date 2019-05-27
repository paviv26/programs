n=str(input())
l1=list()
for i in range(97,123):
    l1.append(chr(i))
for i in range(65,91):
    l1.append(chr(i))
if n in l1:
    print("Alphabet")
else:
    print("No")
    
