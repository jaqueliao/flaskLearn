# 练习项目




### 总结

- 基础命令  
```cmd
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
flask init-db
```
- 生成requirements.txt `pip freeze >requirements.txt`
- 创建一个新的虚拟环境
    `pip install -r requirements.txt`
- 使用waitress运行`waitress-serve --call flaskr:create_app`