"""
该脚本使用开发服务器运行应用程序。
它包含应用程序的路由和视图的定义。
"""

import bilihead
from flask import Flask,redirect
app = Flask(__name__)


wsgi_app = app.wsgi_app


@app.route('/bilihead')
def hello():
    return  redirect(bilihead.getUrl())

if __name__ == '__main__':
    app.run()
