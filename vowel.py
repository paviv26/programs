n=str(input())
l1=list()
l=['a','e','i','o','u','A','E','I','O','U']
for i in range(97,123):
    if chr(i) not in l:
        l1.append(chr(i))
for i in range(65,91):
    if chr(i) not in l:
        l1.append(chr(i))
if n in l:
    print("Vowel")
elif n in l1:
    print("Consonant")
else:
    print("invalid")
    
