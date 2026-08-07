'''
1.URl变量转换器
- 一般URL中的变量默认是字符串，但也可以用转换器改变
- 转换器格式 <type:value>

2.Flask内置的URL变量转换器
- int       整型
- string        不包含斜线的字符串（默认值）
- float     浮点型
- path      包含斜线的字符串
- any       匹配一系列给定值中的一个元素
- uuid      UUID字符串
'''

from flask import Flask
app = Flask(__name__)

# int
@app.route('/hello/<int:age>')
def index(age):
    return f"the int age->{age}"

# path
@app.route('/hello/<path:url>')
def index1(url):
    return f"the string url->{url}"

# 匹配any中的任意一个元素，超出元素页面会报错
@app.route('/hello/<any(tom,jack,myun):name>')
def index2(name):
    return f"my name is: {name}"

# any转换器还可以使用预定义的列表
like = ['book','running','sleep']
@app.route(f'/hello/any({','.join(like)}):like')
def index3(like):
    return f"my love {like}"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)




