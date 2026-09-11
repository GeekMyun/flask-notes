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

3.处理上传文件
- 和普通表单数据不同，文件字段数据上传后文件需要在请求对象的file属性中获取(request.files)
- file属性是Werkzeug中lmmutableMulitDict字典的对象
- file存储字段的name键值和文本对象的映射

4.文件名的处理
- 文件上传如果文件名包含特殊字符或者我们服务器的内部目录，很容易会被上传恶意脚本
- a.使用原文件名：filename=f.filename
- b.使用过滤后的文件名：
  - Werkzeug提供的secure_filename函数可以对文件名进行过滤，传递文件名为参数，该函数
    会过滤所有危险字符，返回安全的文件名
- c.统一重命名：
  - 可以用uuid模块中的uuid4()方法生成新的文件名，并使用hex属性获取十六进制字符串,最后返回包含后缀的文件名
  - uuid.uuid4().hex+ext,ext为文件后缀名

5.文件的保存
- 上传给服务器的文件，需要创建一个保存文件的目录，并将绝对路径配置到自定义变量中
- 调用save()方法保存文件,save(path,file)
"""
from flask import Flask,redirect,url_for,render_template,request,flash,send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed
import os,uuid

app  = Flask(__name__)
app.secret_key="flaskP_wtf"
app.config["MAX_CONTENT_LENGTH"]=3*1024*1024    # 设置最大请求报文3MB


class myforms(FlaskForm):
    file = FileField('图片',validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    submit = SubmitField('上传')

# 处理文件名函数
def random_filename(filename):
    ext=os.path.splitext(filename)[1]
    new_filename=uuid.uuid4().hex+ext
    return new_filename

# 设置文件上传路径
app.config['FILE_PATH']=os.path.join(app.root_path,'files')
@app.route('/file',methods=["GET","POST"])
def index():
    forms = myforms(meta={'locales':'zh'})
    if forms.validate_on_submit():
        f=forms.file.data
        # 生成新的文件名
        filename = random_filename(f.filename)
        # 保存文件
        f.save(os.path.join(app.config['FILE_PATH'],filename))
        flash('file upload sucess')
        return redirect(url_for('show',filename=filename))
    return render_template("day14.html",forms=forms)

# 提供send_from_directory获取上传文件的URL
@app.route('/home/<path:filename>',methods=["GET","POST"])
def get_file(filename):
    return send_from_directory(app.config['FILE_PATH'],filename)

# 显示上传的文件
@app.route('/show',methods=["GET","POST"])
def show():
    filename = request.args.get('filename')
    return render_template('day14_1.html',filename=filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080)
