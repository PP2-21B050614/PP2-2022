s = input()
a, b = s.split()
a = int(a)
b = int(b)
k=0
for i in range(2, a // 2,1):
    if (a % i == 0):
        k = k+1
if k==0 and a<500 and b%2==0:
    print("Good job!")
else:
    print("Try next time!")

'''a=int(input())
b=int(input())

def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

if isitPrime(a)==True and a<500 and b%2==0:
    print("Good job!")
else:
    print("Try next time!")
'''