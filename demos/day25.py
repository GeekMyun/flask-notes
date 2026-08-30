'''
1.jinjia2宏macro
- 模板里面的函数，把重复使用的html代码封装，减低重复性工作

2.宏macro的定义
- 格式：{%macro 名字(参数，默认值)%} 。。。{%endmacro%}

3.宏macro的调用
- 格式：{{宏名(实参)}}

4.宏macro的引入
- 宏macro单独写在一个文件时，需要从外部导入
- from ...import...
- import...as...
- 通过call调用块
'''

from flask import Flask,render_template
app = Flask(__name__)
@app.route('/index')
def index():
    return render_template('day08.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)
