'''appp.route with arguments'''
from flask import Flask
app = Flask(__name__)
@app.route('/home/<name>')
def index(name):
    return f"name {name}"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=False)


