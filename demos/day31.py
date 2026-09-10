"""
自定义校验器
1.行内校验器
- 仅用来校验特定的表单字段
- 从wtforms.validatos模块导入validationErros异常
- 自定义校验器的函数名为validate_xxx的格式

2.自定义校验器运行机制
- 当WTForms执行forms.validate()或者forms.validate_on_submit()时，
  先执行内置校验器
- 然后再扫描表单类，自动查找名字为validate_字段名的方法
- 如果找到就把字段值传进去校验
- validate_字段名靠字段名和表单定义的字段进行交互(validate_name,name)

3.触发条件
- 表单是POST提交
- form.validate_on_submit()执行
- 前面字段基础校验必须先通过

"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegeField,SubmitField
from wtforms.validators import ValidationsError

