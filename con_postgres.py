import psycopg2 as sql
import getpass
from config import config

def connection(status):
    """ Connect to PostgreSQL database server """
    conn = None

    #to open the connection
    if status == 'open':
        try:
            #read connection parameters
            params=config()

            #connect to the postgreSQL
            print('Connecting to the PostgreSQL database...')
            password=getpass.getpass('Password: ')
            conn = sql.connect(**params,password=password)

            #create a cursor
            cur = conn.cursor()
            return cur

        except (Exception, sql.DatabaseError) as error:
            print(error)

    # to close the connection
    elif status == 'close':
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')
    else:
        print('Not an expected comand')
