s=list(input())
d=[]
result=True
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        d.append(s[i])
    else:
        if len(d)==0:
            result=False
            break
        else:
            if s[i]==')' and d[-1]!='(':
                result=False
                break
            elif s[i]=='}' and d[-1]!='{':
                result=False
                break
            elif s[i]==']' and d[-1]!='[':
                result=False
                break
            d.pop(-1)

if(result==False or len(d)>0):
    print("No")
else:
    print("Yes")