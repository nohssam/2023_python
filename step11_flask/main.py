from flask import Flask , send_from_directory

app = Flask(__name__)
@app.route('/')
def index():
    return send_from_directory('html', 'index.html')

@app.route('/<path:name>') # 127.0.0.1/ 이후의 내용은 다 name에 들어온다.
def start(name):
    return send_from_directory('html', name)

app.run(debug=True)