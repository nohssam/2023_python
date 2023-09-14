# flask 설치해야 됨
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서

from flask import Flask
from pandas import DataFrame
import xml.etree.ElementTree as ET
from urllib.request import urlopen


app = Flask(__name__)

spec = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?serviceKey=7Jn37duPnqJP2hXtNvhcywuZlcu2XWgEJYHRSJIIwWps7J94qVJ8gOWdJOJSqoQ9rH2YQCMaCFMtlFsxFPAv8A=='
zcode_list = {'11':'서울','26':'부산','27':'대구',
              '28':'인천','29':'광주','30':'대전','31':'울산',
              '36':'세종','41':'경기','42':'강원','43':'충북',
              '44':'충남','45':'전북','46':'전남','47':'경북','48':'경남',
              '50':'제주'}

@app.route('/')
def index():
    return "hello, worlde"

@app.route('/evChart', methods=['POST'])
def evChart():
    rows = []
    for code in zcode_list.keys():
        res = urlopen(spec+"&zcode="+code).read()

        #결과로 xml문서로 받았으니 xml객체화 시킨다.
        xmlDoc = ET.fromstring(res)

        totalCount = xmlDoc.find('header').find('totalCount').text
        city = zcode_list.get(code)
        # 리스트에 {"code":"11", "city":"서울", "count":"12730"} 형식으로 추가
        rows.append({'code':code, 'city':city, 'count':totalCount})

        df = DataFrame(rows)

    return df.to_json(orient='records')

@app.route("/evCar", methods=['POST'])
def ev_car():
    zcode_dict = {}
    for code in zcode_list:
        res = urlopen(spec+"&zcode="+code).read()

        #결과는 xml문서로 받았다.(res) 이것을 xml문서로 변환해야 함!
        xmlDoc = ET.fromstring(res)

        items = xmlDoc.find("body").find("items")
        totalCount = xmlDoc.find("header").find("totalCount").text

        data_dict = {}

        rows = []
        for item in items:
            statNm = item.find("statNm").text
            chgerType = item.find("chgerType").text
            addr = item.find("addr").text
            rows.append({'s_name':statNm, 'type':chgerType, 'addr':addr})



        #df = DataFrame(rows)
        data_dict["totalCount"] = totalCount
        data_dict["data"] = rows
        zcode_dict[code] = data_dict
        df = DataFrame(zcode_dict)

    return df.to_json(orient='columns')

app.run(debug=True)



