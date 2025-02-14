# 关于
刷小红薯刷到个类似的，借助Py写了一下，可以直接运行dist目录下的exe文件，也可以运行Py文件，大家快拿去骚扰小姐姐哇😃
# 配置
* 想diy的话直接fork，改一改Py源码就行
* 可以将图片和图标设置为自己的 jpg/png/ico……
* 修改完可以用 pyinstaller 生成 exe 可执行文件

# 更新
* 发现别人打开本程序看不到图片，遂意识到图片未打包进exe文件
* v2.0分支改变了项目结构，将图片作为资源嵌入到了exe文件中，直接找到dist目录下的exe文件即可
* 如果想要diy v2.0的图片，将resources下的图片替换并在源码中做相应更改，然后执行“pyinstaller --onefile --windowed --icon=app.ico --add-data="resources/*;resources" love.py”即可
# 忠告
* 正值青春脑子灵
* 哪有时间儿女情
* 献身航空与航天
* 单身十年笑盈盈
