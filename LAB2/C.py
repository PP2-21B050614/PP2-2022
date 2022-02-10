n=int(input())

a=[ [0]*n  for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==0:
            a[i][j]=j
        elif j==0:
            a[i][j]=i
        elif i==j:
            a[i][j]=i*j

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print(end="\n")