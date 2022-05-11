"""
create database database_name
create user name_of_user with password 'password'
grant all privileges on database_name to 'user_name':
"""


import psycopg2


def create_tables():
    command = (
        """
        CREATE TABLE phonebook (
          id serial PRIMARY KEY,
          name VARCHAR (255) UNIQUE NOT NULL,
          phone_number VARCHAR (255) UNIQUE NOT NULL
        );
        """
    )

    conn = None
    try:
    
        conn = psycopg2.connect(dbname='phone', user='phone', password='password)', host='localhost')
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

create_tables()