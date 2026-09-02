"""
1.模板继承
- 多个模板共用部分，可以单独提出作为基模板(父模板)

2.基模板
-格式：{%block name%}...{%endblock%}
- 在block块内插入子模板的内容，{%block son%}...{%endblock%}
- 为了方便代码的阅读，block块可以写成{%block son%}...{%endblock son%}

3.子模板
- 更python的继承一样，使用{%extends farther.html%}继承父模板的内容

4.内容覆盖
- 如果子模板有和同基模板同名的变量或者块，子模板会覆盖基模板

5.内容追加
- 如果子模板想修改基模板内容，可以使用{{super()}}然后追加对基模板的修改
"""
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/index/pag1')
def index():
    return render_template('day09_1.html')

@app.route('/index/pag2')
def index1():
    return render_template('day09_2.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)

