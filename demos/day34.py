"""
1.富文本编辑器
- Flask_CKEditor导入CKEditor类，传入程序实例实现

2.Flask_CKEditor常用配置
- CKEDITOR_SERVE_LOCAL          默认为False，设置为True会使用内置的本地资源
- CKEDITOR_PKG_TYPE             默认为standard，CKEditor包装类型，可选值为basic,standard和full
- CKEDITOR_LANGUAGE             界面语言，传入IOS639格式的语言码
- CKEDITOR_HEIGHT               编辑器高度
- CKEDITOR_WIDTH                编辑器宽度
"""

from flask import Flask,render_template,url_for,redirect
from wtforms import SubmitField
from flask_ckeditor import CKEditor,CKEditorField
from flask_wtf import FlaskForm
from flask_ckeditor.utils import cleanify

app = Flask(__name__)
app.secret_key = "flask"
app.config['CKEDITOR_SERVE_LOCAL']=True
# 初始化CKEditor
ckeditor = CKEditor(app)
class textforms(FlaskForm):
    text = CKEditorField('文本编辑器')
    submit = SubmitField('提交')

@app.route('/index',methods=["GET","POST"])
def  index():
    forms = textforms()
    if forms.validate_on_submit():
        # cleanify函数过滤危险的html,防xss
        safe_content = cleanify(forms.text.data)
        return redirect(url_for('index'))
    return render_template('day15.html',forms=forms)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080)

