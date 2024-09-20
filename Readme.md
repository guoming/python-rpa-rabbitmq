# Rabbitmq 推送

## 1. 项目用途
    基于 Rabbitmq Admin 界面接口 , 读取 CSV 文件内容将数据写入 Rabbitmq

## 2. 配置环境变量
```sh
cat > .env << EOF
RABBITMQ_HOST = ''
USRENAME = ''
PASSWORD = ''
VHOST = ''
EXCHANGE_NAME = 'amq.default'
EOF
```

## 3. 启动
``` python
python src/app.py
```