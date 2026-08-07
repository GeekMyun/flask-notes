'''use default argument in app.route'''
from flask import Flask
app = Flask(__name__)
@app.route('/home',defaults={'name':'jack'})
@app.route('/home/<name>')
def index(name):
    return f"hello {name}"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=False)


'''
@app.route('/home')
@app.route('/home/<name>')
def index(name='jack'):
    return 'hello %s'%name
'''
