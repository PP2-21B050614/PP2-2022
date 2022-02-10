d=[]
for i in range(100000):
    s=input().split()
    if int(s[0])==0:
        break
    d.append(s)
    d[i][0], d[i][2]=d[i][2], d[i][0]
    
for i in range(len(d)):
    for j in range(len(d)-1):
        if int(d[j][0]+d[j][1]+d[j][0])>int(d[j+1][0]+d[j+1][1]+d[j+1][0]):
            d[j], d[j+1]= d[j+1], d[j]

for i in range(len(d)):
        d[i][0], d[i][2]=d[i][2], d[i][0]
for i in range(0,len(d)):
    for j in range(len(d[i])):
        print(d[i][j],end=" ")
    print(end="\n")