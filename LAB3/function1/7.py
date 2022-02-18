s = list(map(int,input().split()))
def has_33(s):
    k=0
    for i in range(len(s)):
        if i>0 and i<len(s)-1:
            if s[i]==3 and s[i-1]==3 or s[i]==3 and s[i+1]==3:
                k+=1
        elif i==0:
            if s[0]==3 and s[1]==3:
                k+=1
        else:
            if s[len(s)-1]==3 and s[len(s)-2]==3:
                k+=1

    if k>0:
        return True
    else:
        return False

print(has_33(s))