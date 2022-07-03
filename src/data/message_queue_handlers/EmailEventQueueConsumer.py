class EmailEventQueueConsumer:
    def __init__(self, channel, emailRepository, byteArrayToDictParser, dictToEmailEventParser,
                       emailEventToJsonParser, emailEventsValidator, emailEventQueueConsumer):
        self._channel = channel
        self._emailRepository = emailRepository
        self._byteArrayToDictParser = byteArrayToDictParser
        self._dictToEmailEventParser = dictToEmailEventParser
        self._emailEventsValidator = emailEventsValidator
        self._emailEventToJsonParser = emailEventToJsonParser
        self._emailEventQueueConsumer = emailEventQueueConsumer

    def set_consumer(self):
        self._channel.queue_declare(queue='email_data_flow')

        self._channel.basic_consume(queue='email_data_flow',
                        auto_ack=True,
                        on_message_callback=self._callback)
    
    def _callback(self, ch, method, properties, body):
        try:
            print(" [x] Received %r" % body)

            body = self._byteArrayToDictParser.parse(body)
            emailEvents = self._dictToEmailEventParser.parse(body)
            
            if (self._emailEventsValidator.validate(emailEvents) == False):
                print(f'{emailEvents} is not valid') # instead throw exception and log
                return
            
            self._emailRepository.add(emailEvents)

            # publish to printing
            jsonBody = self._emailEventToJsonParser.parse(emailEvents)
            self._emailEventQueueConsumer.publish(jsonBody)
            # self._channel.basic_publish(exchange='',
            # routing_key='printing',
            # body=jsonBody)

            print(" [x] Done")
        except Exception as e:
            print(f"Exception : {e}")