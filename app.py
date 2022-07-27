from flask import Flask
from flask import render_template

#環境変数であるenvを最初に設定する
#Windowsのpowershellだと下のコマンドをターミナルにて入力する
#$env:FLASK_APP="ファイル名"
#$env:FLASK_ENV="development"

#インスタンス化
app = Flask(__name__)

#ルートページ
@app.route("/")
def index():
    return render_template("index.html")

#可変のURL
@app.route("/<name>")
def route_name(name):
    return f'<p>Hello, { name }!!!</p>'
