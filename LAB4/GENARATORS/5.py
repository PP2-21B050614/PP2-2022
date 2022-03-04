n = int(input())

def square(n):
    for i in range(0,n+1):
        b=n-i
        yield b

a=square(n)
print(list(a))