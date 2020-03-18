import psycopg2 as sql
import pandas as pd
from con_postgres import connection
from tabulate import tabulate

def flo():

    """Create tabdata for tabFlow"""

    conn=connection('open')
    cur=conn.cursor()

    #Salary by time
    df=pd.read_sql("""
        SELECT DATE,SUM(VALUE) AS VALUE FROM TABFLOW WHERE TYPE='Salario' GROUP BY DATE;
        """,conn)
    print(tabulate(df,headers='keys',tablefmt='psql'),'\n\n')

    #Income and expense by time
    df=pd.read_sql("""
        SELECT DATE,CLASS,SUM(VALUE) AS VALUE FROM TABFLOW GROUP BY DATE, CLASS;
        """,conn)
    print(tabulate(df,headers='keys',tablefmt='psql'),'\n\n')

    #Net profit and eff by time
    """
    df=pd.read_sql(""
        WITH
            TNET_RESULT AS (
                SELECT DATE,
                    SUM(CASE WHEN CLASS='Expense' THEN VALUE*(-1)
                        ELSE VALUE
                    END) AS NET_RESULT
                FROM TABFLOW GROUP BY DATE),

            TINCOME AS (
                SELECT DATE,SUM(VALUE) AS INCOME FROM TABFLOW WHERE TYPE='Salario' GROUP BY DATE)

            SELECT DATE,NET_RESULT FROM TNET_RESULT
            UNION ALL
            SELECT TINCOME.DATE,TINCOME.INCOME FROM TNET_RESULT
            JOIN TNET_RESULT TINCOME ON TNET_RESULT.DATE = TINCOME.DATE;
        "",conn)
    print(tabulate(df,headers='keys',tablefmt='psql'),'\n\n')
    """

    connection('close')

if __name__=='__main__':
    flo()
