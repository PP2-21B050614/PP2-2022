s = input().split()
def rev(s):
    for i in range(len(s)):
        print(s[len(s)-i-1])

rev(s)