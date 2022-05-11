import psycopg2

def update(id, phone_number):
    sql = """
    update phonebook
    set phone_number = %s
    
    where id = %s;
    """
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(dbname='phone', user='phone', password='password)', host='localhost')
        cur = conn.cursor()
        cur.execute(sql, (phone_number, id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

#update(1, 'Aidar')
update(1, '6030969')