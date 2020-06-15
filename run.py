import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask
import os

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True

app.layout=html.Div(children=[html.H1(children='Sample Dash Web App Dashboard'),
                              html.Div(children=''''Dash: A web based app to show Bar Graph'''),
                                      dcc.Graph(id='dash_graph', figure = {'data':[{'x':[1,2,3,4,5],'y':[4,6,3,8,1],'type':'bar','name':'Bread'},
                                                                                    {'x':[1,2,3,4,5],'y':[9,10,11,1],'type':'bar','name':'Bread'},
                                                                                    {'x':[1,2,3,4,5],'y':[4,6,3,8,1],'type':'line','name':'Sugar'},],
                                                                                   'layout':{'title':'Dash Example App'},
                                                                                   }),

dcc.Graph(id='dash_graph', figure = {'data':[{'x':[1,2,3,4,5],'y':[4,6,3,8,1],'type':'bar','name':'Bread'},
                                                                                    {'x':[1,2,3,4,5],'y':[9,10,11,1],'type':'bar','name':'Aeroplane'},
                                                                                    {'x':[1,2,3,4,5],'y':[4,6,3,8,1],'type':'line','name':'Car'},
                                                                                    {'x':[1,2,3,4,5],'y':[4,6,3,8,1],'type':'line','name':'Train'},],
                                                                                   'layout':{'title':'Dash Example App'}})])
