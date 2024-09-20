import csv

import json
import libs.fs as fs


csv_msg_path = 'db/input_mq_receive.csv'
csv_record_path = 'db/input_server_bill_record.csv'
csv_output_path = 'db/output_psc.csv'

dict={}

with open(csv_record_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="\t")
    for row in csvreader:
        dict[row[0]]=1

with open(csv_msg_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="\t")
    row_count = sum(1 for row in csvreader)
    row_index = 0

    csvfile.seek(0)

    for row in csvreader:
        row_index= row_index+1
        route_key=row[0]
        message=row[1]

        msg=json.loads(message)

        if msg.get('shipper_hawbcode') in dict:
            fs.fs_appendLine(csv_output_path, f'{route_key}\t{message}\t{msg.get("shipper_hawbcode")}')

        print(f"\rProgress: {row_index}/{row_count}", end='')

# 完成后换行
print("\nDone!")