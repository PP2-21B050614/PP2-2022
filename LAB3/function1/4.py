s=list(map(int,input().split()))

def filter_prime(*s):
    for i in range(len(s)):
        k=0
        a=int((s[i]**0.5)//1)
        for j in range(2,a+1):
            if s[i]%j==0:
                k+=1
        if k==0 and s[i]!=1 and s[i]!=0:
            print(s[i],end=" ")

filter_prime(*s)