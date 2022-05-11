import psycopg2

conn = psycopg2.connect(dbname='phone', user='phone', password='password)', host='localhost')
cur = conn.cursor()
cur.execute("DELETE FROM phonebook where name='Zora'")
conn.commit()
conn.close()
cur.close()