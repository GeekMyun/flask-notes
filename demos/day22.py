"""
1.Jinja2测试器
- 用来测试变量和表达式的特殊函数
- 格式: value is type，返回Ture或者False的布尔值

2.自定义测试器
- app.template_test(name)

3.Jinja2常用内置测试器
- callable(object)              判断对象是否可被调用
- defined(value)                判断变量是否已被定义
- undefined(value)              判断变量是否未被定义
- none(value)                   判断变量是否为None
- number(value)                 判断变量是否是数字
- string(value)                 判断变量是否是字符串
- sequence(value)               判断变量是否是序列
- iterable(value)               判断变量是否可迭代
- mapping(value)                判断变量是否是匹配对象
- sameas(value,other)           判断变量和other是否指向相同的内存地址
"""
from flask import Flask,render_template,request
app = Flask('__name__')

# 自定义测试器，查看是否成年
@app.template_test('adult')
def is_adult(age):
    try:
        return int(age)>=18
    except:
        return False

@app.route('/index')
def index():
    name=request.args.get('name')
    age=request.args.get('age')
    info={
        'name':name,
        'age':int(age)
    }
    return render_template("day06.html",**info)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)
