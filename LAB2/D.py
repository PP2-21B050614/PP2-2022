n=int(input())

a=[ ['.']*n  for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if n%2==0:
            if i>=j:
                a[i][j]='#'
        else:
            if i>=n-j-1:
                a[i][j]='#'

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end="")
    print(end="\n")