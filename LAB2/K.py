s=list(input().split())
s.sort()
a=[]
for i in range(len(s)):
    d=list(s[i])
    for j in range(len(d)):
        if d[j]=='!' or d[j]==',' or d[j]=='?' or d[j]=='(' or d[j]==')':
            d.remove(d[j])
    for j in range(len(d)):
        if d not in a:
            a.append(d)

print(len(a))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end='')
    print(end="\n")