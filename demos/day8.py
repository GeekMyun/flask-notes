'''
1.请求钩子：
@app.teardown_request    请求结束以后，无论是否报错都执行
-参数接收异常对象exc，没有异常exc就是None
-多用于数据库关闭，释放资源

2.无异常正常流程：
客户端请求--> before_request--> 视图函数@app.route--> after_request (修改响应)--> teardown_request(释放资源)-->浏览器 

3.before_request截断请求：
客户端请求-->before_request-->@app.route-->after_request-->teardown_request-->浏览器 

'''

