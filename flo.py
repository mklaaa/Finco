import psycopg2 as sql
from con_postgres import connection

def flo():

    """Create tabdata for tabFlow"""

    conn=connection('open')
    cur=conn.cursor()

    #First table
    cur.execute('SELECT VERSION ();')
    rec=cur.fetchone()
    print('You are connected to: ',rec)

    connection('close')

if __name__=='__main__':
    flo()
