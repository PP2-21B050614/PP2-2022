class Filt:
    s=[]
    def prime(n):
        if n==1 or n==0:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True

p=Filt
p.s=[1,2,4,5,6,7,8,9,0,11]
d=list(filter(lambda x: p.prime(x),p.s))
print(d)