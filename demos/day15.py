'''
1.Cookie
- Web服务器为了保存某些数据而保存在浏览器上的小型文本数据，浏览器
  会在一定时间内保存它，并在下一次向一个服务器发送请求时带上这些数据

2.Flask中Cookie
- 先make_response手动生成响应对象
- 在使用Response类的set_cookie()方法

3.Responde类的常用属性和方法
- headers           表示响应首部
- status            状态码，文本类型
- status_code       状态码，整型
- mimetype          MIME类型
- set_cookie        设置一个cookie

4.set_cookie()方法的参数
- key               cookie的键(名称)
- value             cookie的值
- max_age           cookie被保存的时间数，以秒为单位，默认在会话结束时过期
- expires           具体的过期时间
- path              限制cookie只能在给定的路径可用，默认为整个域名
- domain            设置cookie可用的域名
- secure            如果设为True，只能通过HTTPS才可以使用
- httponly          如果设为True，禁止客户端JavaScript获取cookie


'''

from flask import Flask,make_response,url_for,redirect,request
app = Flask(__name__)
@app.route('/hello')
def index():
    return 'hello word'

# 保存参数name的值到cookie，并重定向
# 保存后全站点可访问该cookie
@app.route('/user/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('index')))
    # response.set_cookie('name',name,path='/')   默认是 ‘/’，全站可访问
    response.set_cookie('name',name)
    return response

@app.route('/user/<int:age>')
def input_age(age):
    response = make_response('set age to cookie')
    # set_cookie(key,value)里面的value只能是字符串
    # path='/user'，该cookie只能在/user这里使用
    response.set_cookie('age',str(age),path='/user')
    return response

'''
5.Cookie可以通过请求对象的cookies属性读取
'''
@app.route('/cookies')
def get_cookie():
    name = request.cookies.get('name','defaults')
    return f"the cookies is {name}"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)



