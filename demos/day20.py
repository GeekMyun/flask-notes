'''
1.全局对象
- 所有模板都可以使用的对象，包括在模板中导入的模板也可以使用

2.内置全局函数
    - 2.1 jinja2内置模板全局函数
      - range(start,end,step)                   同python的range
      - lipsum(n=5,html=True,min=20,max=100)    生成随机文本，可在测试时用来填充页面
      - dict(**items)                           同python的dict
    
    - 2.2 flask内置模板全局函数
      - url_for()                   用于生成URL的函数
      - get_flashed_messages()      用于获取flash消息函数

3.自定义全局函数
- 使用app.template_global装饰器直接函数注册为全局函数，参数name可以指定一个自定义名称
'''
from flask import Flask,render_template
app = Flask('__name__')

# app.template_global注册的全局函数，在模板中可以直接使用
@app.template_global()
def info():
    info_dict={'name':'tom',
          'age':29}
    return info_dict

@app.route('/info')
def index():
    return render_template('day03.html')

"""
4. get_flashed_messages(with_categories,category_filter)
- flask消息闪现的核心函数，用flash()函数传递函数
- with_categories布尔值，默认False返回消息文本列表，True返回元组列表
- category_filter指定要返回的消息类别
- flash()函数
- 消息取自session，取出来就被清空，只能读取一次
- 必须先配置app.secret_key，否则flash()函数无法使用
"""
from flask import flash,get_flashed_messages,redirect,url_for
app.secret_key='1234'
@app.route('/set')
def set_msg():
    # 存入消息和消息类别
    flash('操作成功','sucess')
    flash('参数错误','error')
    return redirect(url_for('get_msg'))
@app.route('/get')
def get_msg():
    # 简单文本
    msg1 = get_flashed_messages()
    print(f"文本类型消息->{msg1}")
    # 获取带类型的消息
    msg2 = get_flashed_messages(with_categories=True)
    print(f"dict类型->{msg2}")
    # 获取指定类型的消息
    msg3 = get_flashed_messages(category_filter='error')
    print(f"error->{msg3}")
    return str(msg3)


@app.route('/hello')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
