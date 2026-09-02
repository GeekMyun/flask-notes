'''
表单的渲染
- 要在模板中渲染表单，首先要将实例化的表单传给模板
- 表单传给模板后就可以转化为HTML代码，在页面上渲染出来
'''

from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

app = Flask(__name__)
app.secret_key='wtforms'

class Forms(FlaskForm):
    username = StringField(label='账号',validators=[DataRequired(message='usernane not is none')],
                           render_kw={'placeholder':'请输入~'})
    password = PasswordField('密码',validators=[DataRequired(),Length(6,12)])
    submit = SubmitField('',render_kw={'value':'登录'})

@app.route('/index')
def index():
    forms=Forms()
    # 通过render_template()传递表单给模板
    return render_template('day10.html',forms=forms)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)

