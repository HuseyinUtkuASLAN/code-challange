class PrintQueuePublisher:
    def __init__(self, channel):
        self._channel = channel

    def set_publisher(self):
        self._channel.queue_declare(queue='printing')
        
    def publish(self, jsonBody):
        self._channel.basic_publish(exchange='',
            routing_key='printing',
            body=jsonBody)