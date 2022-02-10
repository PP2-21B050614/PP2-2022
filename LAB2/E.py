s = input().split()
if len(s)!=2:
    n=int(s[0])
    x=int(input())
else:
    n, x = s
    n = int(n)
    x = int(x)

a=[0]*n
k=0
for i in range(n):
    a[i]=x+2*i
    k=k^a[i]

print(k)