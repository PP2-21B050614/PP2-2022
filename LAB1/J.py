s=string=input()
x=s.split(' ')
for i in range(0,len(x)):
    if len(x[i])>=3:
        print(x[i],end=' ')
