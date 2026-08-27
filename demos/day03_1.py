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

"""
2.URl查询参数
- request.args
- ?a=xx&b=xx格式
"""
from flask import request
@app.route('/demo')
def index1():
    name = request.args.get("name")
    age = request.args.get("age",default=0,type=int)
    return f"name={name},age={age}"

"""
3.JSON请求体，接口传参
- request.get_json()
"""
@app.route('/api/test',methods=["POST"])
def index2():
    data = request.get_json()
    a=data.get("a")
    b=data.get("b")
    return {"res":a+b}

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)

