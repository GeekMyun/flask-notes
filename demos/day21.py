"""
1.过滤器
- 在模板内对变量进行格式化
- 格式：{{变量|过滤器}}，{{变量|过滤器(参数)}}
- 过滤器只能在模板中使用，视图函数中不能用

2.自定义过滤器
- app.template_filter()
"""

from flask import Flask,render_template
app = Flask(__name__)
@app.route('/info/<name>')
def index(name):
    # 参数要传入到模板中才能使用
    return render_template("day04.html",name=name)

# 自定义过滤器，参数指定别名
@app.template_filter('filter_test')
def index2(str):
    return str[::-1]


"""
2. jinja2常用内置过滤器
- default(value,default_value='xxx',boolean=False)      设置默认值，默认值作为参数传入，别名为d
- escape(s)                                             转义html文本，别名为e
- first(seq)                                            返回序列的第一个元素
- last(seq)                                             返回序列的第一个元素
- length(object)                                        返回变量的长度
- random(seq)                                           返回序列中的随机文本
- safe(value)                                           将变量值标记安全，避免转义
- trim(value)                                           清除变量值前后的空格
- max(value,case_sensitive=False,attribute=None)        返回序列中的最大值
- min(value,case_sensitive=False,attribute=None)        返回序列中的最小值
- striptags(value)                                      清楚变量值内的HTML标签
- unique(value,case_sensitive=False,attribute=None)
- urlize(value,trim_url_limit=None,nofollow=False,target=None,rel=None)     将URL文本转换为可单机的HTML的链接
- wordcount(s)                                          计算单词数量
- tojson(value,indent=None)                             将变量值转换为JSON格式
- truncate(s,length=255,killwords=False,end='..',leeway=None)       截断字符串，常用于显示文章摘要，length参数设置
  截取的长度，killwords参数设置是否截断单词，end参数设置结尾的符号
"""
from flask import request,flash,redirect,request,render_template,get_flashed_messages,url_for
app.secret_key='1234'
@app.route('/login',methods=['POST','GET'])
def login():
    # 如果是POST表示表单提交数据过来了
    if request.method == "POST":
        # 获取提交的数据，表单中要有name属性才能拿到数据
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age')
        if not username:
            flash('username is None','error')
            return redirect(url_for('login'))     # 返回登录界面
        print(f"username->{username}\n,password->{password},age->{age}")
        return f"""
        <p>提交成功</p>
        <p>username:{username}</p>
        <p>password:{password}</p>
        <p>age:{age}</p>
        <a href='/login'>登录</a>
        """
    # 如果是GET请求直接去login界面
    return render_template("day05.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)

