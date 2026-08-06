'''
1.请求钩子：
after_request    视图执行完，响应返回给浏览器之前执行
-不能截断请求，必须接收respone参数，并且返回return respone
-如果before_request截断请求，视图函数不执行，after_request会执行

2.基本用途：
-统一添加响应头
-统一修改Cookie，所以接口统一设置cookie
-统一日志，记录响应状态码
-统一修改返回内容
'''

from flask import Flask 
app = Flask(__name__)

@app.before_request  
def frist():
    print('befefore_request')

@app.route('/')
def index():
    return 'hello'

@app.after_request
def last(resp):
    # resp是后端要返回给浏览器的响应对象
    print('after_request run -> status_code is',resp.status_code)
    # 也可以修改响应头
    resp.headers["X-Demo"] = 'hello_after'
    # 一定要return resp,要不然页面报错
    return resp

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)

'''
befefore_request
after_request run -> status_code is 200
'''

