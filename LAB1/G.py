
a=input()
s=0
b=len(a)
for i in a:
    s=s+int(i)*pow(2,b-1)
    b=b-1

print(s)

''''
solution with integer

a=int(input())
s=0
n=a
k=0
while n!=0:
    n=n//10
    k=k+1

for i in range(0,k,1):
    s=s+pow(2,i)*(a%10)
    a=a//10

print(s)
'''