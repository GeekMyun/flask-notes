"""
WTForm表单
- WTF对比自己写表单，给我们提供了很多方便，例如CSRF防护，后端校验，表单渲染，表单回填

1.使用
- 继承从flask_wtf导入FlaskForm类，用python类实现WTF表单
- Form自带很多字段(Filed)，相当于html表单的各个属性
- 实例化表单类就可以实现html的转换
- 通过label渲染我们需要的表单
"""

"""
2.常用的WTF字段
- BooleanField          复选框，值会被处理为True或False             <input type="checkbox">
- DateField             文本字段，值会被处理为datetime.date对象     <input type="text">
- DateTimeField         文本字段，值会被处理为datetime.datetime对象 <input type="text">
- FileField             文件上传字段                                <input type="file">
- FloatField            浮点数字段，值为处理为浮点型                <input type="text">
- IntegerField          整数字段，值为处理为整型                    <input type="text">
- RadioField            一组单选按钮                                <input type="radio">
- SelectField           下拉列表                                    <select><option></option></select>
- SelectMultipleField   多选下拉框                                  <select multiple><option></option></select>
- SubmitField           提交按钮                                    <input type="submit">
- StringField           文本字段                                    <input type="text">
- HiddenField           隐藏文本字段                                <input type="hidden">
- PasswordField         密码文本字段                                <input type="password">
- TextAreaField         多行文本字段                                <textarea></textarea>
"""

"""
2.1.字段格式
- 完整格式：字段名(label,validators=[校验器1,校验器2],**kwargs)
- label             表单显示的文字(form.xxx.label输出)，可以传字符串，也可以不写“”
-validators=[]      校验器列表，做后端校验，也可以为空列表[]
- **kwargs          额外参数，id,clss,value等属性，用render_kw={}添加需要的属性
"""

"""导入Form和常用的字段"""
from wtforms import StringField,PasswordField,BooleanField,SubmitField

"""
3.采用的WTF校验器(validator)
- DataRequired(message=None)                         验证数据是否有效
- Email(message=None)                               验证Email地址
- EqualTo(fieldname,message=None)                   验证两个字段值是否相同
- InputRequired(message=None)                       验证是否有数据
- Length(min=-1,max=-1,message=None)                验证输入值长度是否在给定范围内
- NumberRange(min=None,max=None,message=None)       验证输入数字是否在给定范围内
- Option(strip_whitespace=True)                     允许输入值为空，并跳过其他验证
- Regexp(regex,flags=0,message=None)                使用正则表达式验证输入值
- URL(require_tld=True,message=Nonde)               验证URL
- AnyOf(values,message=None,values_formatter=None)  确保输入值在可选值列表中
- NoneOf(values,message=None,values_formatter=None) 确保输入值不在可选值列表中
"""

"""导入常用的校验器"""
from wtforms.validators import DataRequired,Length
from flask_wtf import FlaskForm

# 创建表单类
class Myform(FlaskForm):
    # message参数用来传入错误提示的消息
    username = StringField('username',validators=[DataRequired(message=u'username不能为空！')])
    password = PasswordField('password',validators=[DataRequired(),Length(6,12)])
    submit = SubmitField('submit',render_kw={'value':'sub'})

"""
4.实例化字段类常用的参数
- label             字段标签<label>的值，也就渲染后显示在输入字段前的文字
- render_kw         一个字典，用来设置HTML标签的属性
- validators        一个列表，包含一系列验证器，会在表单提交后被逐一调用验证表单数据
- default           字符串或可调用对象，用来为字段设置默认值
"""

"""
5.输出HTML代码
- 实例化表单，然后将实例属性转换成字符串或直接调用就可以获取表单字段对应的HTML代码
- 字段的<label>元素的HTML代码则可以通过"form.字段名.label"的形式获取
"""

from flask import Flask
app = Flask(__name__)
app.secret_key="1234"

"""
6.添加属性
- 使用render_kw添加，username=StringField(label='username',render_kw={'placeholder':'请输入～'})
- 在调用字段时传入
"""
@app.route('/index')
def index():
    # 实例化表单,要在视图函数内实例，需要上下文
    myform=Myform()
    # 转化为HTML代码
    print(f"username:{myform.username()}")
# username:<input id="username" name="username" required type="text" value="">
    print(f"username:{myform.username(style='width:20px',placeholder='请输入～')}")
# username:<input id="username" name="username" placeholder="请输入～" required style="width:20px" type="text" value="">
    print(f"password:{myform.password()}")
# password:<input id="password" maxlength="12" minlength="6" name="password" required type="password" value="">
    print(f"submit:{myform.submit()}")
# submit:<input id="submit" name="submit" type="submit" value="sub">
    
    # 输出label
    print(f"username:{myform.username.label()}")
# username:<label for="username">username</label>
    print(f"password:{myform.password.label()}")
# password:<label for="password">password</label>
    print(f"submit:{myform.submit.label()}")
# submit:<label for="submit">submit</label>

    return 'WTForm'

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)
