'''
1.Jinja2
- 把后端python的数据，填充到HTML网页里面，生成完整网页给浏览器显示
- 默认模板目录是在项目的同级目录，文件名必须叫templates，小写，不能写错

2.Jinja2常见的三种定界符
- {{表达式}}：输出渲染，把变量，表达式结果输出到网页
- {% 依据 %}：控制语句，if,for,block,extends,macro,只执行逻辑，不输出内容，必须闭合结束标签
- {# 注释内容 #}：模板注释

3.Jinja2常见的for循环特殊变量
- loop.index        当前迭代数，从1开始计数
- loop.index0       当前迭代数，从0开始计数
- loop.revindex     当前反向迭代数，从1开始计数
- loop.revindex0    当前反向迭代数，从0开始计数
- loop.first        如果是第一个元素，则为True
- loop.last         如果是最后一个元素，则为True
- loop.previtem     上一条迭代的条目
- loop.nexitem      下一条迭代的条目
- loop.length       序列包含的元素数量

4.渲染模板
- 执行模板中的代码，并传入所有在模板中使用的变量，渲染的结果
  返回给浏览器的HTML响应
- 视图函数渲染模板时，使用render_template()渲染函数
- 使用render_template_string()函数渲染模板字符串

5.渲染函数
- render_template：读取templates文件的html文件，交给jinja渲染
 第一个参数表示要渲染的html文件，后面的键值对参数表示向后端模板传变量
- render_template_string()：不读取html文件，直接把字符串当做jinja2模板来渲染
 第一个参数表示模板文本字符串，后面参数同样可以传参数
'''
from flask import Flask,render_template,render_template_string
app = Flask(__name__)
def add(num):
    total = 0
    for i in range(1,num+1):
        total+=i
    return total

# render_template
@app.route('/demo')
def demo():
    name = 'myun'
    age = 25
    total = add(10)
    return render_template('day01.html',name=name,age=age,total=total)

# render_template_string
@app.route('/demo1')
def demo1():
    html = """
        <h1>hello word</h1>
        <h2>{{name}}</h2>
        <h2>{{age}}</h2>
        <h2>one add to ten:{{total}}</h2>
        """
    return render_template_string(html,name='tom',age='19',total=add(10))
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
         

