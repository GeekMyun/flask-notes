"""
WTForm表单
- WTF对比自己写表单，给我们提供了很多方便，例如CSRF防护，后端校验，表单渲染，表单回填

1.使用
- 基于wtforms的Form类，用python类实现WTF表单
- Form自带很多字段(Filed)，对于html表单的各个属性
- 实例化表单类就可以实现html的转换
- 通过label渲染我们需要的表单
"""
from flask import Flask
app = Flask(__name__)

"""导入Form和常用的字段"""
from wtforms import Form,StringFiled,PasswordFiled,BooleanFiled,SubmitFiled

"""导入常用的校验函数"""
from wtforms.validators import DataRquired,Length

class baseform(Form):
    username = Form('username',validators=[DataRquired()])
    password = Form('password',validators=[DataRquired(),Length(6,12)])
    number = Form('number')

