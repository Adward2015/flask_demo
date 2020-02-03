# -*- coding: utf-8 -*-
"""
使用简单网页模板的flask
实现简单的登录
返回带有数据的html网页
"""
from flask import Flask, render_template, redirect, request, session
from utils import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "I love Adward"


@app.route('/')
@login_required
def hello_world():
    return 'Hello, stranger!'


@app.route('/hello')
@login_required
def hello_user():
    tmp = {"user": session.get("user_info")}
    # 将数据传入到页面中
    return render_template("hello.html", data=tmp)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        req_username = request.form.get("user")
        req_pwd = request.form.get("password")
        if req_username == "1" and req_pwd == "1":
            # 设置session
            session.update(user_info=1)
            # 如果是在其他页面登录的(登录页面除外),则跳转到对应的页面
            if session.get("redirect"):
                return redirect(session.get("redirect"))
            return redirect("/")
        else:
            return "用户名密码错误"
    return render_template('login.html')


if __name__ == '__main__':
    # host填全0是为了其他电脑也能通过IP进行访问
    app.run(debug=True, host="0.0.0.0", port=5555)
