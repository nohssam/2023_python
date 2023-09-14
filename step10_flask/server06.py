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
        # f-string 사용법
        # 1. 문자열 앞에 f를 붙인다.
        # 2. 문자열 중간에 변수나 계산식을 넣을 수 있다. (중괄호{}를 이용하면 )
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

@app.route('/read/<id>')
def read(id):
    return '<h2> Read %s </h2>' %id

# 디버깅 실행 형식
app.run(debug=True)
