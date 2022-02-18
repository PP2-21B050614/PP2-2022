s = list(map(int,input().split()))
def spy_game(s):
    f=0
    for i in range(len(s)):
        if s[i]==7:
            d=0
            for j in range(i):
                if s[j]==0:
                    d+=1
            if d==2:
                f+=1
    if f>0:
        return True
    else:
        return False

print(spy_game(s))