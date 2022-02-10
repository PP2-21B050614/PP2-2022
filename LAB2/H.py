a, b=input().split()
a=int(a)
b=int(b)
n=int(input())

d = []
for i in range(n):
    d.append([int(j) for j in input().split()])

for i in range(len(d)):
    for j in range(len(d)-1):
        if ((a-d[j][0])**2+(b-d[j][1])**2)**0.5>((a-d[j+1][0])**2+(b-d[j+1][1])**2)**0.5:
            d[j], d[j+1] = d[j+1], d[j]
            
for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j],end=" ")
    print(end="\n")