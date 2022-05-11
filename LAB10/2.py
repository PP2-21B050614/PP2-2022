import psycopg2
#truncate table table_name restart identity - clear to table
with open('LAB10/phone.csv','r') as f:
    text=str(f.read())
    d=text.split()
    phone_list=[]
    for i in range(len(d)):
        phone_list.append(tuple(d[i].split(',')))

def insert_new(list):
    sql = """
    insert into phonebook(name, phone_number) values (%s, %s);
    """

    conn = None
    try:

        conn = psycopg2.connect(dbname='phone', user='phone', password='password)', host='localhost')
        cur = conn.cursor()
        cur.executemany(sql, list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

insert_new(phone_list)