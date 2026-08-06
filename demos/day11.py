'''
1.Request对象
- request对象封装了从客户端发来的请求报文，可以从request对象这里获取请求报文中的所有数据

2.使用request对象的属性获取请求URL
以http://GeekMyun.com/hello?name=Myun为例
| 属性    |   值
- path      'hello'
- full_path     'hello?name=Myun'
- host      'GeekMyun.com'
- host_url      'http://GeekMyun.com/'
- base_url      'http://GeekMyun.com/hello'
- url       'http://GeekMyun.com/hello?name=Myun'
- url_root      'http://GeekMyun/'
'''

from flask import Flask,request
app = Flask(__name__)
@app.route('/hello')
def index():
    url = request.url
    return f"请求报文url-->{url}"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)











