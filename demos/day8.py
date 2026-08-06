'''
1.请求钩子：
@app.teardown_request    请求结束以后，无论是否报错都执行
- 参数接收异常对象exc，没有异常exc就是None
- 不需要return,
- 多用于数据库关闭，释放资源

2.无异常正常流程：
客户端请求--> before_request--> 视图函数@app.route--> after_request (修改响应)--> teardown_request(释放资源)-->浏览器 

3.before_request截断请求：
客户端请求-->before_request-->@app.route-->after_request-->teardown_request-->浏览器 

4.试图函数抛出异常
before_request--> 视图函数抛出异常--> after_request不执行--> teardown_request拿到exc异常，一定会执行
'''

from flask import Flask
app = Flask(__name__)

@app.before_request
def before_hock():
    print('before_request run...')

@app.route('/')
def index():
    return 'hello'      # 视图函数必须要写return

@app.after_request
def after_hock(resp):
    print('after_request run...')
    return resp

@app.teardown_request
def tear_hock(exc):
    print('teardown_request run exc-->',exc)
    # return在这里无效

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)

'''
before_request run...
after_request run...
teardown_request run exc--> None

'''



