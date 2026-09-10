"""
自定义校验器
1.行内校验器
- 仅用来校验特定的表单字段
- 从wtforms.validatos模块导入validationErros异常
"""

from flask import Flask
from flask_wtf import FlaskForm
