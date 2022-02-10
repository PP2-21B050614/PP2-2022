n=int(input())

d=[]
for i in range(n):
    s=input()
    k=0
    c=0
    f=0
    for i in s:
        if i>='a' and i<='z':
            k=k+1
        elif i>='A' and i<='Z':
            c=c+1
        elif i>='0' and i<='9':
            f=f+1
    if k>0 and c>0 and f>0 and s not in d:
        d.append(s)

d.sort()
print(len(d))
for i in range(len(d)):
    print(d[i])

