# Simple piece of code to delete message queue from rabbitMQ

import pika
host = '10.10.1.14'
creds = pika.PlainCredentials('openstack', 'su123')
params = pika.ConnectionParameters(host, credentials=creds)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_delete(queue='foo.info')

connection.close()
