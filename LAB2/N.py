d=[]
while True:
    n=int(input())
    if n==0:
        break
    d.append(n)

for i in range(len(d)//2):
    d[i]=d[i]+d[-1]
    d.pop(-1)
for i in range(len(d)):
    print(d[i],end=" ")