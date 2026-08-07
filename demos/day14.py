'''
1.响应格式
- HTTP响应中，数据可以通过多种格式传输
- 不同的格式需要设置不同的MIME类型
- MIME类型在首部的Content-Type字段中定义，如：Content-Type:text/html;charset=utf-8

2.MIME类型
- 是一种用来识别文件类型的机制，一般格式：类型名/子类名称
- 通过Flask通过的make_respones()方法生成响应对象，传入响应的主体作为参数
- 然后通过响应对象的mimetype属性设置MIME类型
'''

from flask import Flask,make_response,json
app = Flask(__name__)
@app.route('/mimetype')
def index():
    response = make_response('hello world')    # 生成响应对象respone
    response.mimitype = 'text/plain'
    # 也可以直接设置首部字段来设置
    # respone.headers['Content-Type'] = 'text/xml;charset=utf-8'
    return response

'''
3.常见的MIME类型
- 纯文本        text/plain
- HTML          text/html
- XML           application/xml 
- JSON          application/jsion
'''

@app.route('/html')
def index1():
    html = "<h1>hello word</h1>"
    response = make_response(html)
    response.mimetype = 'text/html'
    return response

@app.route('/text')
def index4():
    text = '<h1>hello word</>'
    response = make_response(text)
    response.mimetype = 'text/plain'
    return response

@app.route('/xml')
def index2():
    xml ='''<?xml version='1.0' encoding='UTF-8'?>
    <note>
    <tips>hello</tips>
    <tip>word</tip>
    </note>
    '''
    response = make_response(xml)
    response.mimetype = 'application/xml'
    return response

@app.route('/json')
def index3():
    json = {
        'note':{
            'tips':'hello',
            'tip':'word'
            }
            }
    response = make_response(json)
    return response

'''
JSON格式还可以直接从Flask导入json对象，然后调用dumps()方法将字典，列表
或者元组系列序列化为JSON字符串
'''
@app.route('/json1')
def index5():
    data = {
            'name':'myun',
            'like':'code'
            }
    response = make_response(json.dumps(data))
    return data

'''
也可以使用jsonify函数，直接将传入的参数和数据转为json字符串作为响应主体
并且自动设置正确的MIME类型
'''
from flask import jsonify
@app.route('/json2')
def index6():
    return jsonify(name='myun',like='code',skill='python')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
    
