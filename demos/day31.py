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

4.全局校验器
- 和行内校验器相同，只不过写在表单外
- 在定义字段时在validators里传入全局校验器名
"""

from flask import Flask,render_template,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import ValidationError,DataRequired,Length,NumberRange

app = Flask(__name__)
app.config['WTF_I18_ENABLED']=False
app.secret_key='flaskdemo'

# 全局校验器
def is_age(form,field):
    if field.data < 18:
        raise ValidationError('未成年~')

class myform(FlaskForm):
    name = StringField('用户名',validators=[DataRequired('not null')],render_kw={'placeholder':'username!'})
    age = IntegerField('年龄1',validators=[NumberRange(12,50)])
    age1 = IntegerField('年龄2',validators=[is_age])  # 在validators列表里面添加全局校验器
    submit = SubmitField('提交')
    # 行内校验器
    def validate_age(self,field):
        if field.data < 18:
            raise ValidationError('未成年~')

@app.route('/index',methods=["POST","GET"])
def index():
    forms = myform(meta={'locales':['zh']})
    if forms.validate_on_submit():
        return redirect(url_for('hello'))
    return render_template('day13.html',form=forms)

@app.route('/hello',methods=["GET","POST"])
def hello():
    return "提交成功！"

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)

