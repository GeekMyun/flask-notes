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

from flask import Flask,make_response
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
-XML            application/xml 
'''



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
    
