import psycopg2 as sql
from con_postgres import connection

cur=connection('open')
cur.execute('SELECT VERSION ();')
rec=cur.fetchone()
print('You are connected to: ',rec)

connection('close')
