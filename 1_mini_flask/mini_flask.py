# -*- coding: utf-8 -*-
"""
最小版本的flask程序,运行端口5555
运行之后,输入http://localhost:5555/就可以访问
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    # host填全0是为了其他电脑也能通过IP进行访问
    app.run(host="0.0.0.0", port=5555)
