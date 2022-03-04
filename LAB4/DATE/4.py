from datetime import datetime
a=datetime(2022, 1, 12)
b=datetime(2018, 5 , 16)
x=a.day*60*60*24+a.month*30*60*60*24+a.year*365*30*60*60*24
y=b.day*60*60*24+b.month*30*60*60*24+b.year*365*30*60*60*24
print(x)
print(y)
print(x-y)