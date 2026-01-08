# 使用官方 Python 轻量级镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 暴露端口 (Flask 默认 5000, 但云平台通常会提供 PORT 环境变量)
EXPOSE 5000

# 启动命令 (使用 gunicorn 生产级服务器)
CMD gunicorn --bind 0.0.0.0:$PORT app:app
