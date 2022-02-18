s=list(input())
f=[]
f=s
answer=[]
def Permuttaion(s):
    for i in range(len(s)):
        for j in range(len(s)):
            s = f
            if s[i]!=s[j]:
                s[i], s[j] = s[j], s[i]
                d=""
                for k in range(len(s)):
                    d=d+s[k]
                
                if d not in answer:
                    answer.append(d)

Permuttaion(s)
print(answer,end="\n")