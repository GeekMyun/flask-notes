'''
设置监听的HTTP方法
1.视图函数监听的方法：
- GET  获取资源
- POST  提交新增资源
- PUT  全局替换更新
- PATCH  局部更新
- DELETE  删除
- HEAD  获取响应头，不要响应体
- OPTIONS  跨越预检，查询服务器允许哪些方法
- TRACE  调试，隧道代理
- CONNECT  调试，隧道代理

2.用app.route的methodsc参数传入一个监听方法设置监听，如果请求的方式不符合要求，请求会无法被正常处理
'''

from flask import Flask
app = Flask(__name__)
@app.route('/',methods=['GET','POST','PUT'])
def index():
    return 'hello world'

@app.teardown_request
def tear(exc):
    print('访问方式错误：',exc)

'''
@app.teardown_appcontext
def tear(exc):
    print('访问方式错误：',exc)
'''

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)






