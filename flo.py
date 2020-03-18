import psycopg2 as sql
import pandas as pd
from con_postgres import connection
from tabulate import tabulate

def flo():

    """Create tabdata for tabFlow"""

    conn=connection('open')
    cur=conn.cursor()

    #First table
    """
    cur.execute('SELECT VERSION ();')
    rec=cur.fetchone()
    print('You are connected to: ',rec)
    """

    df=pd.read_sql('SELECT * FROM TABFLOW LIMIT 5;',conn)
    print(tabulate(df,headers='keys',tablefmt='psql'))

    connection('close')

if __name__=='__main__':
    flo()
