"""
1.处理表单数据的一般顺序(获取数据到保存数据)
- 解析请求，获取表单数据
- 对数据进行必要的转换
- 验证数据是否符合要求，同时验证CSRF令牌
- 如果验证未通过则需要生成错误消息，并在模板中显示错误消息
- 如果通过验证，就把数据保存到数据库或进一步处理

2.提交表单
- 当<form>标签的类型为submit时点击会创建一个提交表单的html请求
- HTML表单中控制提交行为的属性
  - action      默认值当前URL，即页面对于的URL
  - method      默认为get，提交表单的HTTP请求方法
  - enctype     默认值为application/x-www-form-urlencoded,请求表单的编码类型，当
    表单中包含文件上传字段时，需要设置为multipart/form-data，还可以设置为纯文本
    类型text/plain

3.验证表单数据
- Flask-WTF验证表单一般分为客户端验证和服务器端验证(WTForms)
- 客户端验证：指在客户端对用户输入的值进行验证
- 服务器端验证：指用户把输入的数据提交到服务器端，在服务器端对数据进行

4.WTForms验证机制
- 在实例化表单类时传入表单数据，然后对表单实例调用validate()方法
- 调用方法后会逐个对字段实例化时定义的验证器，返回表示验证结果的布尔值
- 如果验证失败，就把错误消息存储到表单实例的errors属性对应的字典里

5.表单中的提交方式获取
- 使用POST方法提交的表单，其数据会被Flask解析为一个字典，可以通过请求对象的form
  属性获取(request.form)
- 使用GET方法提交的表单数据同样会被解析为字典，不过要通过请求对象的args属性获取(request.args)

6.在视图函数中验证表单
- 试图函数中同时可以接收两种类型的请求，所以要根据不同的请求方法执行不同的代码
- 如果时GET请求，那么就渲染模板
- 如果是POST请求，就调用validate()验证表单数据
- Flask-WTF提供的validate_on_submit()方法，可以合并数据提交和数据验证，且使用所有请求类型

7.错误消息
- 没有通过验证的字段，WTF会把错误消息添加到表单类的erros属性中
- 一般可以直接通过字段名获取对应字段的错误消息列表(form.fieldname.errors)

"""

from flask import Flask,request,render_template,redirect,url_for
from wtforms import (StringField,PasswordField,SubmitField,BooleanField
,DateField,FileField,IntegerField,RadioField,SelectField,TextAreaField)
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,NumberRange

app = Flask(__name__)
app.secret_key="wtforms"        # CSRF保护需要设置密钥

# 表单类,继承FlaskForm类
class Forms(FlaskForm):
    username = StringField(label='用户名',validators=[DataRequired('账号不能为空')],render_kw={'placeholder':'请输入~'})
    password = PasswordField(label='密码',validators=[Length(6,12)])
    age = IntegerField(label='年龄',validators=[Length(9,11)])
    # RadioField和SelectField核心参数:choices=['传给后端的值','页面显示文字']
    sex = RadioField(label='性别',choices=[('1','男'),('2','女')],default='1',validators=[DataRequired('请选择性别')])
    home = SelectField(label='省份',choices=[('sz','深圳'),('cd','成都'),('sh','上海')],)
    birth = DateField('出生日期')
    submit = SubmitField(label='提交')
    area = TextAreaField(label='个性签名')

@app.route('/login',methods=['POST','GET'])
def login():
    form = Forms()
    if request.method =="POST" and form.data.validate():  # 验证表单
        redirect(url_for('index'))
    return render_template('day11.html',form=form)

# 使用form.validate_on_submit()验证表单数据
@app.route('/login1',methods=['POST','GET'])
def login1():
    form = Forms()
    if form.validate_on_submit():
        redirect(url_for('index'))
    return render_template('day11.html',form=form)

@app.route('/index',methods=['POST','GET'])
def index():
    return 'hello word'

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)








