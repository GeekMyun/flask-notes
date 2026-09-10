""""
文件上传
1.HTML文件件上传
- 标签input的type='file'用来上传文件，其中的accept属性可以过滤文件类型

2.Flask_WTF表单文件上传
- 文件上传字段FileFeild
- 文件上传验证器
  - FileRequired(message=None)          验证是否包含文件对象
  - FileAllowed(upload_set,message=None)            用来验证文件类型，upload_set参数
    用来传入包含允许的文件后缀名列表
- 文件大小验证：配置变量MAX_CONTENT_LENGTH可以限制请求报文的最大长度
- 表单包含文件上传字段时，需要将表单的enctype属性设为'multipart/form-data',告诉
  浏览器将上传数据发送到服务器，否则仅会把文件名作为表单数据提交

"""
from flask import Flask,redirect,url_for,render_template,request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed

app  = Flask(__name__)
app.secret_key="flaskP_wtf"
app.config["MAX_CONTENT_LENGTH"]=3*1024*1024    # 设置最大请求报文3MB


class myforms(FlaskForm):
    file = FileField('图片',validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    submit = SubmitField('上传')

@app.route('/file',methods=["GET","POST"])
def index():
    forms = myforms(meta={'locales':'zh'})
    print(f"{request.files}")
    if forms.validate_on_submit():
        return redirect(url_for('home'))
    print(f"{forms.errors}")
    return render_template("day14.html",forms=forms)

@app.route('/home',methods=["GET","POST"])
def home():
    return "文件上传成功！"


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080)
