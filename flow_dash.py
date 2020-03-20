import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from tabulate import tabulate
from flow import flow
import dash
import dash_core_components as dcc
import dash_html_components as html

def flow_dash():
    df={}

    df=flow()

#    print(df['income'])
#    for i in df:
#        print('\n',tabulate(df[i],headers='keys',tablefmt='psql'))

#    fig = go.Figure()
#    fig.add_trace(go.Scatter(x=df[0]['date'],y=df[0]['income']))
#    fig.show()

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

#    fig = go.Figure(data=go.Scatter(x=df['date'],y=df['income']))
#    fig.show()

if __name__=='__main__':
    flow_dash()
