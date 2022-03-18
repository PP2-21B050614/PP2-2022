s=input()
c=0
m=0
for i in s:
    if i>='a' and i<='z':
        c=c+1
    elif i>='A' and i<='Z':
        m=m+1
print(c,m)