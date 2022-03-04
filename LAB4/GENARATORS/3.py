n = int(input())

def even(n):
    for i in range(0,n+1,3):
        if i%4==0:
            yield i

a=even(n)
print(list(a))