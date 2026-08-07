'''
1.请求钩子：
@app.teardown_appcontext     应用上下文销毁时执行

2.teardown_appconext和teardown_request区别
- tearddown_request每一次请求结束，请求上下文销毁执行
- teardown_appcontext是应用上下文销毁执行，不一定跟着HTTP请求
- web正常的情况下，一次http请求会同时生成请求上下文和应用上下文，请求结束两个请求一起销毁，两个钩子一起都会执行
- 在离线情况下，没有http请求，手动with app.app_context(),代码块结束，应用上下文被销毁，只会执行teardown_appcontext，不会执行teardown_reaquest
'''

# 常见的用来关闭数据库
# Flask_SQLAlchemy官方示例：用来回收会话，避免数据库连接泄漏
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
