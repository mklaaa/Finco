import psycopg2 as sql
from config import config
import numpy as np

def connect():
    """ Connect to PostgreSQL database server """
    conn = None
    try:
        #read connection parameters
        params=config()

        #connect to the postgreSQL
        print('Connecting to the PostgreSQL database...')
        conn = sql.connect(**params)

        #create a cursor
        cur = conn.cursor()

    #execute a statement
        cur.execute('SELECT VERSION();')
        rec=cur.fetchone()
        print('PostgreSQL database version:',rec)

        #close the communication with the PostgreSQL
        cur.close()
    except (Exception, sql.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__=='__main__':
    connect()
