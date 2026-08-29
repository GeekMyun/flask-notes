"""
局部慢板
- 在其他慢板里面插入多个慢板共用的慢板，简化代码
- 用include标签插入局部慢板
"""

from flask import Flask,render_template
app = Flask(__name__)
@app.route('/index/<user>')
def index(user):
    return render_template('day07.html',user=user)


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)
