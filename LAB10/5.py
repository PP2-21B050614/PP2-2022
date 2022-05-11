from queue import Empty
import psycopg2

conn = psycopg2.connect(dbname='phone', user='phone', password='password)', host='localhost')
cur = conn.cursor()
#cur.execute("SELECT * FROM phonebook where id=3")
cur.execute("SELECT * FROM phonebook where phone_number='369410'")
#cur.execute("SELECT * FROM phonebook where name='Rinat'")
results = cur.fetchall()
if not results:
    print("not in the table")
else:
    print(results)
conn.close()
cur.close()