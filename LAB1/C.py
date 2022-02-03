s=input()

def tolower(s):
    for i in s:
        if 'A'<=i<='Z':
            print(chr(ord(i)+32),end='')
        else:
            print(i,end='')

tolower(s)