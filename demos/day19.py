'''
1.模板上下文变量
- 函数render_template()手动传入变量，还是Flask中默认传入的变量，
  都是模板上下文变量

2.上下文内容
- 手动传入的变量
- Flask自带内置上下文变量
- 注册到全局的函数，app.add_template_global(func),
  函数加入上下文，模板可以直接调用

3.Flask内置上下文变量
- config            读取app配置
- request           请求对象
- session           session会话
- g                 flask的g对象

4.常见的上下文传参方式
- render_template关键字传参
- dict字典解包

5.自定义上下文变量
- 使用{{% set %}}定义变量，仅当前模板生效，语法：{%set key=value%}
- set块赋值，把一大段赋值给变量，{%set value%}{%endset%}，调用{{value}}
- 全局自定义变量app.context_processor，所有上下文自带该变量

'''
from flask import Flask,render_template
app = Flask(__name__)

# render_template关键字传参
@app.route('/demo')
def index():
    return render_template('day02.html',username='myun',PL='python')

# dict字典解
@app.route('/demo1')
def index1():
    dic = {
        'phone':'apple',
        'color':'blue',
        'price':'10000$'
    }
    return render_template('day02-1.html',**dic)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)

