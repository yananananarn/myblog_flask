from re import A
from flask import Flask
from flask import render_template

#環境変数であるenvを最初に設定する
#Windowsのpowershellだと下のコマンドをターミナルにて入力する
#$env:FLASK_APP="ファイル名"
#$env:FLASK_ENV="development"

#インスタンス化
app = Flask(__name__)

bullets={
    "箇条書き1",
    "箇条書き2",
    "箇条書き3",
    "箇条書き4",
    "箇条書き5",
    "箇条書き6"
}

#ルートページ
@app.route("/")
def hello_yana():
    return render_template("index.html", bullets=bullets)

#可変のURL
@app.route("/<name>")
def route_name(name):
    return f'<p>Hello, { name }!!!</p>'
