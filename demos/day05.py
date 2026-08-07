'''urls to one view_function '''
from flask import Flask
app = Flask(__name__)
@app.route('/hi')
@app.route('/hello')
def index():
    return 'hello word'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=False)
