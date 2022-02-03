a=int(input())
c=input()
if c=='b':
    print(a*1024)
elif c=='k':
    x=int(input())
    print(round(a/1024,x))