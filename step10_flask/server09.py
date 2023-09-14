# flask 설치해야 됨
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서
from urllib.parse import urlencode
import pandas as pd
from flask import Flask,jsonify
from urllib.request import urlopen, Request
#https://docs.python.org/ko/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
params = '?' + urlencode({'serviceKey' : '7Jn37duPnqJP2hXtNvhcywuZlcu2XWgEJYHRSJIIwWps7J94qVJ8gOWdJOJSqoQ9rH2YQCMaCFMtlFsxFPAv8A==', 'pageNo' : '1', 'numOfRows' : '10', 'zcode' : '11' })
request = Request(url+params)
response_body = urlopen(request).read()
root = ET.fromstring(response_body)
df = pd.DataFrame()
# 현재 엘리먼트를 루트로 하여 트리 이터레이터를 만듭니다.
# root.iter('time')
for item in root.iter('item'):
    item_dict={}
    item_dict['충전소명'] = (item.find('statNm').text)
    item_dict['주소'] = item.find('addr').text
    item_dict['위도'] = item.find('lat').text
    item_dict['경도'] = item.find('lng').text
    item_dict['충전기상태'] = (item.find('stat').text)

    df = df._append(item_dict, ignore_index=True)

app = Flask(__name__)
@app.route('/')
def index():
    return "hello, worlde"

@app.route('/car')
def car():
    return df.to_string()

app.run(debug=True)

