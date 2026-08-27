"""
视图函数传入多个参数
- URl路径参数
- 查询字符串
- 表单POST
- JSON请求体
"""

from flask import Flask
app = Flask(__name__)

"""
1.URl路径参数
- 路由里面写，多个路径参数用<>包裹
"""
@app.route('/hello/user/<name>/age/<int:age>')
def index(name,age):
    dict = {
        'name':name,
        'age':age
    }
    return dict




if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)

