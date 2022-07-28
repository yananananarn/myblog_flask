from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

#環境変数であるenvを最初に設定する
#Windowsのpowershellだと下のコマンドをターミナルにて入力する
#$env:FLASK_APP="ファイル名"
#$env:FLASK_ENV="development"

#インスタンス化
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

#モデルの定義
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  body = db.Column(db.String(300), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

#ルートページ
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        posts = Post.query.all()
        return render_template("index.html", posts = posts)

    return render_template("index.html")

#記事作成
@app.route("/create", methods=['GET','POST'])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")

        post = Post(title=title, body=body)
        
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("create.html")

#編集ページ
@app.route("/<int:id>/update", methods=['GET','POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == "GET":
        return render_template("update.html", post = post)
    else:        
        post.title = request.form.get("title")
        post.body = request.form.get("body")
        
        db.session.commit()
        return redirect("/")

#削除
@app.route("/<int:id>/delete", methods=['GET','POST'])
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect("/")

#可変のURL
"""
@app.route("/unchi/<name>")
def route_name(name):
    return f'<p>Hello, { name }!!!</p>'
"""

if __name__ == "__main__":
    app.run(debug=True)