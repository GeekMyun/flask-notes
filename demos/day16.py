'''
1.session：安全的cookie
- session指用户会话，又称用户对话，及服务器和客户端/浏览器之间
  或桌面程序和用户之间建立的交互活动
- 在Flask中，session对象用来加密Cookie，默认情况下，它会把数据
  存储在浏览器上一个名为session的cookie里

2.session通过密钥对数据进行签名以加密数据，密钥是一种具有一定复杂度和
随机性的字符串，在Flask中一般这样设置：
- 通过Flask.secret_key属性
- 通过配置SECRET_KEY设置
'''

from flask import Flask,redirect,session,url_for
app = Flask(__name__)
# 设置加密解码密钥
app.secret_key = 'my-secret'
@app.route('/hello')
def hello():
    return 'hello word'

@app.route('/login')
def login():
    # session对象可以向字典一样操作
    session['login_in'] = True   # 将login_in写入session，并赋值为True
    return redirect(url_for('hello'))

# 获取session
@app.route('/check')
def check():
    sessions = session.get('login_in')
    return f"get session is {sessions}"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
