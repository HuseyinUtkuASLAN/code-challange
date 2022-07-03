from models.EmailEvent import EmailEvent
import pika

class EmailEventQueueHandler:

    def Init(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='email_data_flow')

    def publish(self, email_event : EmailEvent):
        self.channel.basic_publish(exchange='',
            routing_key='email_data_flow',
            body= email_event.toJSON())
