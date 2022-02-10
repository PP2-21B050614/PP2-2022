a=input().split()
k=0
for i in range(0,len(a)):
    if i==k:
        k=int(a[i])+k

if k>=len(a):
    print(1)
else:
    print(0)