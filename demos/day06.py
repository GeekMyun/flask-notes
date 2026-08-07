'''
1.请求钩子：
@app.befor_request   在请求到达视图之前执行
- 返回非null，截断请求，试图函数不会被执行
- 返回null，继续执行试图函数

2.常见用途：
- 登录校验
- 请求统一日志，记录访问信息
- 全局权限校验
- 设置全局变量，所有模板，路由使用
'''

from flask import Flask
app = Flask(__name__)

# befor_request
@app.before_request
def hook():
    print('------befor_request run------')
   # return not null  试图函数不会被执行

# 注册路由
@app.route('/hello')
def index():
    print('-----index run------')
    return 'hello'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=False)

'''
------befor_request run------
-----index run------
'''

