'''flask base template'''
# 1. input flask base class Flask
from flask import Flask

# 2. create the application instance
app = Flask(__name__)   # flie name --> __name__

# 3. register the route
@app.route('/home')
def index():
    return 'hello word!'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=False)

