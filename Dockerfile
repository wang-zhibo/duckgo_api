# 使用官方的 Python 3.11 镜像作为父镜像
FROM python:3.11

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录的内容复制到容器中的 /app 目录
COPY . /app

# 升级 pip 并安装依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 暴露 FastAPI 默认端口 9400
EXPOSE 9400

# 运行 FastAPI 服务
CMD ["python", "duckgo_fastapi_server.py"]

