import pandas as pd
from tabulate import tabulate
from flow import flow
import dash
import dash_core_components as dcc
import dash_html_components as html

def flow_dash():

    """Dashboard for Cashflow"""
    
    df={}
    df=flow()

    print(df['income'])
    #for i in df:
    #    print('\n',tabulate(df[i],headers='keys',tablefmt='psql'))

"""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout=html.Div([
        dcc.Graph(
            figure={
                'data':[
                    dict(
                        x=df['date'],
                        y=df['income'],
                        type='bar'
                    )
                ]
            }
        )
    ])

    app.run_server(debug=True)
"""
if __name__=='__main__':
    flow_dash()
