n=int(input())
d=""
for i in range(1,n+1):
    s=input()
    x=s.find("@gmail.com")
    if x>0:
        d=d+s[0:x]+"\n"

print(d)