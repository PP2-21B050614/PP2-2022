from datetime import datetime, timedelta
x=datetime.now()
b=x - timedelta(days=5)
print(b.strftime("%Y-%m-%d"))