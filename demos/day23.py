"""
1.jinja2.Environment环境模板变量
- 存储过滤器，测试器，全局函数，模板语法符，等配置

2.核心字典
- app.jinja_env.filters             存放过滤器|
- app.jinja_env.tests               存放测试器 is
- app.jinja_env.globals             存放模板全局函数/变量
"""
from flask import Flask
app = Flask(__name__)

# 1.使用环境模板变量注册过滤器
def my_filter(s):
    return s.upper()
# 等价 @app.template_filter('myfilter')
app.jinja_env.filters['myfilter'] = my_filter

# 2.使用环境模板变量注册测试器
def my_test(age):
    return int(age)>=18
# 等价 @app.template_test('mytest')
app.jinja_env.tests['mytest'] = my_test

# 3.修改变量符号
app.jinja_env.varibale_start_string = "[["
app.jinja_env.varibale_end_string = "]]"

# 4.修改语句块符号
app.jinja_env.block_start_string = "[%"
app.jinja_env.block_end_string = "%]"
# 更改后模板里面就要写[[value]],[%block%],不过只是临时更改，重启flask恢复默认值

# 5.注册全局函数(globals)
def hello():
    return 'hello word'
app.jinja_env_globals['hello'] = hello

# 6.去掉模板多余空白行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# 7.关闭自动转义（不推荐）
app.jinja_env.autoescape = False
