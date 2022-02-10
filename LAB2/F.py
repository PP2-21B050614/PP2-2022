n=int(input())

d={ }

for i in range(n):
    s, x=input().split()
    x=int(x)
    if s in d:
        d[s]+=x
    else:
        d[s]=x

a=list(d.keys())
b=d.values()
m=max(b)
a.sort()
for i in a:
    if d[i]==m:
        print(i+"is lucky!")
    else:
        print(i+"has to receive "+str(m-d[i])+" tenge")
