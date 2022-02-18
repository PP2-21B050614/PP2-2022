s = list(map(int,input().split()))

def histogram(s):
    for i in range(len(s)):
        for j in range(s[i]):
            print('*',end='')
        print(end="\n")
histogram(s)