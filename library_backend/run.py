from app import create_app  # 从app包导入create_app函数

app = create_app()  # 创建Flask应用

if __name__ == "__main__":
    app.run(debug=True)  # 启动服务，开启调试模式