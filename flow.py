import psycopg2 as sql
import pandas as pd
from con_postgres import connection
from tabulate import tabulate

def flow():

    """Create tabdata for Cashflow"""

    conn=connection('open')
    #cur=conn.cursor()

    #Income by time
    df=pd.read_sql("""
        SELECT DATE,SUM(VALUE) AS VALUE FROM TABFLOW WHERE TYPE IN ('Salario','Bonus') GROUP BY DATE;
        """,conn)
    print(tabulate(df,headers='keys',tablefmt='psql'),'\n\n')

    #Total income and expense by time
    df=pd.read_sql("""
        SELECT DATE,CLASS,SUM(VALUE) AS VALUE FROM TABFLOW GROUP BY DATE, CLASS;
        """,conn)
    print(tabulate(df,headers='keys',tablefmt='psql'),'\n\n')

    #Net profit and eff by time
    df=pd.read_sql("""
        CREATE TEMP TABLE T1 AS SELECT DATE,SUM(VALUE) AS INCOME FROM TABFLOW WHERE CLASS='Income' GROUP BY DATE;
        CREATE TEMP TABLE T2 AS
        	SELECT DATE,
        		SUM(CASE WHEN CLASS='Expense' THEN VALUE*(-1)
        			ELSE VALUE
        		END) AS NET_RESULT
        	FROM TABFLOW GROUP BY DATE;
        SELECT *,(T2.NET_RESULT/T1.INCOME) AS EFF FROM T1 NATURAL JOIN T2;
        """,conn)
    print(tabulate(df,headers='keys',tablefmt='psql'),'\n\n')

    connection('close')

if __name__=='__main__':
    flow()
