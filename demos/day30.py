"""
1.为错误消息设置语言
- 不使用flask_babel翻译，仅使用Flak内置翻译器，设置为False
- 然后在自定义的基类中定义Meta类，并在locales列表中进入中文语言的地区字符串
- 最后我们自定义的表单基础基类，实现错误消息语言的设置
"""

from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key='forms'
app.config['WTF_I18N_ENABLED'] = False

class mybaseform(FlaskForm):
    class Meta:
        locales=['zh']    # 简体中文zh,繁体中文zh_wtf

class myform(mybaseform):
    username = StringField(label='用户名',validators=[DataRequired()],render_kw={'placeholder':'请输入~'})
    submit = SubmitField(label='提交')

# 正常meta设置locales修改错误消息语言
@app.route('/index',methods=["POST","GET"])
def index():
    form = myform()
    if forms.validate_on_submit():  # 验证表单
        redirect(url_for('hello'))
    return render_template("day12.html",form=form)

# 在实例化表单时通过meta关键字传入locales值设置错误消息语言
@app.route('/index1',methods=["POST","GET"])
def index1():
    form = myform(meta={'locales':['zh']})
    if form.validate() and request.method=="POST":
        redirect(url_for('hello'))
    return render_template('day12.html',form=form)

@app.route('/hello')
def index2():
    return "提交成功！"

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)
