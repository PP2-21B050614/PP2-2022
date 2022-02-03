s=string=input()
c=char=input()
x=s.find(c)
b=0
for i in s:
    if i==c:
        b=b+1
    
if b>=2:
    k=s.rfind(c)
    print(x,k)
elif b==1:
    print(x) 