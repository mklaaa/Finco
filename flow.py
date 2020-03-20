#import psycopg2 as sql
import pandas as pd
from con_postgres import connection
from tabulate import tabulate
import plotly.graph_objects as go

def flow():

    """Create tables for Cashflow"""

    conn=connection('open')
    #cur=conn.cursor()

    df={}

    #Income by time
    df[0]=pd.read_sql("""
        SELECT DATE,SUM(VALUE) AS INCOME FROM TABFLOW WHERE TYPE IN ('Salario','Bonus') GROUP BY DATE;
        """,conn)
    #print('\n',tabulate(df[0],headers='keys',tablefmt='psql'),'\n\n')

    #fig = go.Figure()

    #fig.add_trace(go.Scatter(x=df[0]['date'],y=df[0]['income']))
    #fig.show()

        #Total income and expense by time
    df[1]=pd.read_sql("""
        SELECT DATE,CLASS,SUM(VALUE) AS VALUE FROM TABFLOW GROUP BY DATE, CLASS;
        """,conn)
    #print(tabulate(df[1],headers='keys',tablefmt='psql'),'\n\n')

    #Net profit and eff by time
    df[2]=pd.read_sql("""
        CREATE TEMP TABLE T1 AS SELECT DATE,SUM(VALUE) AS INCOME FROM TABFLOW WHERE CLASS='Income' GROUP BY DATE;
        CREATE TEMP TABLE T2 AS
        	SELECT DATE,
        		SUM(CASE WHEN CLASS='Expense' THEN VALUE*(-1)
        			ELSE VALUE
        		END) AS NET_RESULT
        	FROM TABFLOW GROUP BY DATE;
        SELECT *,(T2.NET_RESULT/T1.INCOME) AS EFF FROM T1 NATURAL JOIN T2;
        """,conn)
    #print(tabulate(df[2],headers='keys',tablefmt='psql'),'\n\n')

    connection('close')

    return df[0]

if __name__=='__main__':
    flow()
