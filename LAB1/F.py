a=int(input())
s=""
for i in range(1,a+1,1):
    b=int(input())
    if b<=10:
        s=s+"Go to work!"+"\n"
    elif 10<b and b<=25:
        s=s+"You are weak"+"\n"
    elif 25<b and b<=45:
        s=s+"Okay, fine"+"\n"
    elif b>45:
        s=s+"Burn! Burn! Burn Young!"+"\n" 

print(s)