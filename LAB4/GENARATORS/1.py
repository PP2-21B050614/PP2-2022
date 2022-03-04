n = int(input())

def square(n):
    for i in range(1,n+1):
        b=i*i
        yield b

a=square(n)
print(list(a))