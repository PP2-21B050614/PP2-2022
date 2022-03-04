n = int(input())

def even(n):
    for i in range(0,n+1,2):
        yield i

a=even(n)
b = list(a)
for i in range(len(b)):
    if i == len(b)-1:
        print(b[i])
    else:
        print(b[i],end=',')