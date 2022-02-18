s = list(input().split())
answer=[]
def unique(s):
    for i in range(len(s)):
        if s[i] not in answer:
            answer.append(s[i])
unique(s)
print(answer)