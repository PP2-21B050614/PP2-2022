a = int(input())
b = int(input())
def squares(a,b):
    for i in range(a,b+1):
        c=i*i
        yield c

d=squares(a,b)
print(list(d))
