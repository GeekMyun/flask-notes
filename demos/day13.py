'''
1.响应报文
- falsk程序中，客户端发出请求触发相应的视图函数，获取返回值会作为响应的主体，最后服务器生成完-整的响应报文

2.响应报文组成
- 协议版本
- 状态码（status code）
- 原因短语（reason phrase）
- 响应首部
- 获取返回值会作为响应的主体

3.常见的HTTP状态码
|   状态码   |  原因短语   |    说明    |
- 成功
  - 200         ok          请求被正常处理
  - 201         Created     请求被处理，并创建一个新资源
  - 204         No Content  请求处理成功，但无内容返回

- 重定向
  - 301         Moved Permanently   永久重定向
  - 302         Found               临时性重定向
  - 304         Not Modifiled       请求的资源未被修改，重定向到缓存的资源
  
- 客户端错误
  - 400         Bad Request         表示请求无效，即请求报文存在错误
  - 401         Unauthorized        类似403，表示请求的资源需要获取授权信息，在浏览器中会弹出认证弹窗
  - 403         Forbiden            表示请求的资源被服务器拒绝访问
  - 404         Not Found           表示服务器上无法找到请求的资源或URL无效

- 服务区错误
  - 500         Internal Server Error       服务器内部发生错误

4.在Flask 中生成响应 
- 响应在Flask中使用Request对象表示，响应报文中的内容大多数由服务器处理
- Flask会判断是否可以找到与请求URL相匹配的路由，如果没有返回404，如果找到则调用对应的视图函数，视图函数的返回值构成了响应报文的主体内容
- 正常返回状态码默认为200，Flask会调用make_response()方法将视图函数返回值转换为响应对象
- 视图函数可以返回最多三个元素组成的元组：响应主体，状态码，首部字段

'''

from flask import Flask,redirect,url_for,abort
app = Flask(__name__)
@app.route('/hello')
def index():
    return 'hello word'    # 默认状态码是200

# 修改状态码
@app.route('/hi')
def index1():
    return 'hi word',204

# 修改状态码后，可以用Location字段设置重定向都URL
@app.route('/baidu')
def index2():
    return f"go to ->baidu",302,{'Location':'http://www.baidu.com'}

'''
5. redirect函数实现重定向
- 使用redirect实现重定向默认是302
- 如果想修改状态可以在redirect函数的code关键字传入
- 如果想重定向到其他视图函数可以用url_for生成目标URL  
'''

# redirect函数重定向
@app.route('/huawei')
def index3():
    return redirect('https://www.huawei.com')

# 模拟404跳转
@app.route('/404')
def index4():
    print('no fond ！go to hello pag')
    # redirect状态码通过code修改，重定向状态码：301~308，其他的不行
    # url_for(视图函数名)-->得到目标视图函数的URL
    return redirect(url_for('index'),code=301)

'''
6.错误响应
- 正常情况下，Flask会自动常见错误响应，抛出这些异常即可返回对应的错误响应
- abort()函数可以手动返回错误响应，只要传入状态码即可
'''
@app.route('/403')
def index5():
    abort(403)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
