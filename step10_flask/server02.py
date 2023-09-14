# flask 설치해야 됨
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서

from flask import Flask
app = Flask(__name__)

# 태그 사용 가능
@app.route('/')
def hello_world():
    return '<h2>Hello World!~~~~~~</h2>'

@app.route('/makeup')
def makeup():
    return 'makeup~~~'

@app.route('/data')
def data():
    return 'data~~~~~'
# 원래 실행 형식
# if __name__ == '__main__':
#     app.run()

# 디버깅 실행 형식
app.run(debug=True)