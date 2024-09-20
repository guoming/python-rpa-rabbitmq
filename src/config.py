import os
from dotenv.main import load_dotenv

load_dotenv()

rabbitmq_host = os.getenv('RABBITMQ_HOST')
print("RABBITMQ_HOST:", rabbitmq_host)

username = os.getenv("USERNAME")
print("USERNAME:", username)

password = os.getenv("PASSWORD")
print('PASSWORD:', password)


vhost = os.getenv("VHOST")
print('VHOST:', vhost)

exchange_name = os.getenv("EXCHANGE_NAME")
print('EXCHANGE_NAME:', exchange_name)