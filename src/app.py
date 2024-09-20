import csv

import requests
import json
import libs.fs as fs
import config

# 定义发送消息的URL
url = f"{config.rabbitmq_host}/api/exchanges/{config.vhost.replace('/','%2F')}/{config.exchange_name}/publish"

# 打开CSV文件并读取内容
csv_file_path = 'db/input.csv'
csv_output_error_path = 'db/output_error.csv'
csv_checkpoint_path= 'db/checkpoint'

with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="\t")
    row_count = sum(1 for row in csvreader)
    row_index=0
    row_index_checkpoint= fs.fs_read(csv_checkpoint_path)
    error_count=0;

    # 重置文件指针到文件开头
    csvfile.seek(0)

    for row in csvreader:
        row_index=row_index+1

        if row_index<=int(row_index_checkpoint):
            continue

        # 将每一行转换为字符串，准备作为消息
        routing_key=row[0]+"@Failed"
        message=row[1]

        payload={
            "vhost":config.vhost,
            "name":config.exchange_name,
            "properties":{"delivery_mode":1,"headers":{}},
            "routing_key":routing_key,
            "delivery_mode":"1",
            "payload": message,
            "headers":{},
            "props":{},
            "payload_encoding":"string"
        }

        # 通过HTTP接口发送消息
        response = requests.post(url, auth=(config.username, config.password), headers={'Content-Type': 'application/json'},
                                 data=json.dumps(payload))

        # 检查响应状态
        if not response.status_code == 200:
            fs.fs_appendLine(csv_output_error_path, f"{routing_key}\t{message}\t")
            error_count=error_count+1

        fs.fs_write(csv_checkpoint_path, str(row_index))

        # 输出进度条，\r 回到行首，end='' 防止自动换行
        print(f"\rProgress: {row_index}/{row_count}, error={error_count},success={row_index-error_count}", end='')


# 完成后换行
print("\nDone!")