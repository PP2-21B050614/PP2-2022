n=int(input())

d={ }

for i in range(n):
    s, x=input().split()
    if x in d:
        d[x]+=1
    else:
        d[x]=1

a=int(input())

for i in range(a):
    f, e, num=input().split()
    num=int(num)
    if e in d:
        d[e]=max(0,d[e]-num)
    
live=sum(list(d.values()))
print("Demons left:",live)