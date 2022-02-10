n=int(input())

d = []
f = []
for i in range(n):
    s=list(input().split())
    a=int(s[0])
    
    if a==2 and len(d)!=0:
        f.append(d[0])
        d.pop(0)
    elif a==1:
        d.append(s[1])

for i in range(len(f)):
    print(f[i],end=" ")

