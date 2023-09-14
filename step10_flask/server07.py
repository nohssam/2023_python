import random

from flask import Flask
from urllib.parse import urlencode
import requests
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

app = Flask(__name__)

# 나중에 DB 읽엉는 코드로 변경된다.
menu = [
    {'id':1, 'title':'HTML', 'body': 'html is ...'},
    {'id':2, 'title':'CSS', 'body': 'css is ...'},
    {'id':3, 'title':'JS', 'body': 'javascript is ...'}
]

@app.route('/')
def index():
    liTags = ""
    for i in menu:
        liTags = liTags + f'<li><a href="/read/{i["id"]}">{i["title"]}</a></li>'
    return f'''
      <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Welcome</h2>
                Hello, Web
            </body>
        </html>
    '''

@app.route('/create')
def create():
    return '<h2> Create </h2>'

# 파라미터는 string 인데 int로 변경 해준다.(<int:id>)
@app.route('/read/<int:id>')
def read(id):
    liTags = ""
    for i in menu:
        liTags = liTags + f'<li><a href="/read/{i["id"]}">{i["title"]}</a></li>'

    title=''
    body=''
    for i in menu:
        if id == i['id']:
            title = i['title']
            body = i['body']
            break

    return f'''
         <!doctype html>
            <html>
                <body>
                    <h1><a href="/">WEB</a></h1>
                    <ol>
                        {liTags}
                    </ol>
                    <h2>{title}</h2>
                   {body}
                </body>
            </html>
    '''

# 디버깅 실행 형식
app.run(debug=True)
