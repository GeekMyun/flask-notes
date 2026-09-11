"""
多文件上传
- 在客户端的input标签加入multiple属性
- 表单中使用WTForms提供的MultipleField字段实现
- 在获取上传的文件时使用request.files的getlist方法
"""

from flask import Flask,url_for,redirect,render_template
from flask_wtf import FlaskForm
from wtforms import MultipleField,SubmitField
from wtforms.validators import DataRequird,Length
import os,uuid

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH']=10*1024*1024
app.secret_key="flask_wtf"

class myforms(Flask):
    files = MultipleField("文件",validators=[DataRequird])
    submit = SubmitField("提交")

@app.route("/file",methods=["POST","GET"])
def index():
    forms = myforms(meta={'locales':'zh'})
