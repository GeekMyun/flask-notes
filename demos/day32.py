""""
文件上传
1.HTML文件件上传
- 标签input的type='file'用来上传文件，其中的accept属性可以过滤文件类型

2.Flask_WTF表单文件上传
- 文件上传字段FileFeild
- 文件上传验证器
  - FileRequired(message=None)          验证是否包含文件对象
  - FileAllowed(upload_set,message=None)            用来验证文件类型，upload_set参数
    用来传入包含允许的文件后缀名列表
- 文件大小验证：配置变量MAX_CONTENT_LENGTH可以限制请求报文的最大长度
- 表单包含文件上传字段时，需要将表单的enctype属性设为'multipart/form-data',告诉
  浏览器将上传数据发送到服务器，否则仅会把文件名作为表单数据提交
"""
