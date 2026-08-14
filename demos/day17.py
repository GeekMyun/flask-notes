'''
1,Flask上下文
- 应用上下文application context --> 保存Flask应用示例的环境
- 请求上下文request context --> 保存一次HTTP请求独有的信息：浏览器提交的信息，
    Cookie，本次会话session
    - 请求来了：压入栈
    - 请求结束：全部销毁

2.应用上下文变量
- current_app       指向处理当前程序实例
- g                 代替python的全局变量用法，确保仅当前请求中可用，用于
                    存储全局数据，每次请求都会被重设

3.请求上下文变量
- request       封装客户发出来的请求报文
- session       用于记住请求之间的数据，通过签名的Cookie实现
'''

from flask import Flask,request,session,g,current_app
app = Flask(__name__)

'''
4.request保存浏览器发来的http全部信息，url，get参数，post表单，headers，cookie
必须在请求上下文内使用
'''
@app.route('/hello/<name>')
# /hello/myun?age=25
def index(name):
    args = request.args  # age=25
    headers = request.headers
    cookies = request.cookies
    return f"args-->{args},headers->{headers},cookies->{cookies}"

'''
5.session用户会话
'''
app.secret_key='my-secret'
@app.route('/set_session')
def set_session():
    session['name'] = 'myun'
    return 'set session is ok'

@app.route('/get_session')
def get_session():
    return session.get('name')

'''
6.current_app代表当前运行的Flask应用实例，等价代码里的app,
  不能在模块顶部使用，必须上下文激活
'''
@app.route('/test')
def current():
    key = current_app.secret_key
    name = current_app.name
    return f"key->{key},name->{name}"
# key->my-secret,name->day17

'''
7.g是视图函数之间传递临时数据的媒介，只存在后端内存，换一个请求就清空，
  同一个请求链路里数据共享
'''

# 钩子给视图函数传数据
@app.before_request
def info():
    g.name = 'myun'
    g.age = 25

@app.route('/get_g')
def get_g():
    name = g.name
    age = g.age
    return f'name->{name},age->{age}'

'''
8.激活上下文
- 想使用上下文变量，要先激活上下文，否则直接报错RuntimeError
- 应用上下文变量current_app,g要应用上下文激活
- 请求上下文变量request,session要请求上下文激活
- 只要激活了请求上下文，会自动把应用上下文也推上去
- 但是是激活应用上下文，不会激活请求上下文
'''
'''
9.三种激活情况
- 1.浏览器访问，Flask收到HTTP请求，推送请求上下文，请求上下文内部
     自动推送应用上下文
'''
@app.route('/demo')
def demo():
    # 全部可用，上下文自动激活
    print(current_app.secret_key)
    g.name = 'tom'
    print(request.path)
    session['name'] = 'jack'
    return 'all contexts is ok '

'''
- 2.只手动开启应用上下文：app.app_context()
'''
with app.app_context():
    print('application_context is ok ->',current_app.secret_key)

'''
- 3.开启请求上下文：app.test_request_context()，会附带开启应用上下文
'''
with app.test_request_context('/'):
    print('request_context is ok ->',current_app.secret_key)
    g.name = 'lisa'
    print(request.path)
    session['like'] = 'sleep'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)



