class PrintQueuePublisher:
    def __init__(self, channel, byteArrayToDictParser, cache):
        self._channel = channel
        self._byteArrayToDictParser = byteArrayToDictParser
        self._cache = cache

    def set_consumer(self):
        self._channel.queue_declare(queue='printing')

        self._channel.basic_consume(queue='printing',
                auto_ack=True,
                on_message_callback=self._callback)
        
    def _callback(self, ch, method, properties, body):
        body = self._byteArrayToDictParser.parse(body)
        print(body)
        self._cache.append(body) 
