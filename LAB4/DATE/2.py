from datetime import datetime, timedelta
x=datetime.now()
b=x - timedelta(days=1)
c=x + timedelta(days=1)
print(b.strftime("%Y-%m-%d"))
print(x.strftime("%Y-%m-%d"))
print(c.strftime("%Y-%m-%d"))