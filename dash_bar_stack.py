# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

cc = pd.read_csv("spending_17.csv", sep='\t',header=[0,1])
print cc.head()

trace1 = go.Bar(x=cc.index, y=cc[('amount','business services')], name='business services')
trace2 = go.Bar(x=cc.index, y=cc[('amount','credit card payment')], name = 'credit card payment')
trace3 = go.Bar(x=cc.index, y=cc[('amount','groceries')], name='groceries')
trace4 = go.Bar(x=cc.index, y=cc[('amount','home phone')], name='home phone')
trace5 = go.Bar(x=cc.index, y=cc[('amount','rental car & taxi')], name='rental car & taxi')
trace6 = go.Bar(x=cc.index, y=cc[('amount','restaurants')], name='restaurants')
trace7 = go.Bar(x=cc.index, y=cc[('amount','shopping')], name='shopping')
trace8 = go.Bar(x=cc.index, y=cc[('amount','travel')], name='travel')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children="Spending Report"),
    html.Div(children="2017 spending by category"),
    dcc.Graph(
        id = 'spending_vs_category',
        figure = {
            'data' : [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8],
            'layout': go.Layout(title='Spending by Category', barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
