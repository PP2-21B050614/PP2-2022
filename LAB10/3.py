import psycopg2

def insert_new(name, phone_number):
    sql = """
    insert into phonebook(name, phone_number) values (%s, %s);
    """

    conn = None
    try:

        conn = psycopg2.connect(dbname='phone', user='phone', password='password)', host='localhost')
        cur = conn.cursor()
        cur.execute(sql, (name, phone_number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
 
while True:
    s=str(input())
    n, p =s.split(',')
    insert_new(n,p)
    if s=="0":
        break
