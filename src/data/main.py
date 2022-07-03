#!/usr/bin/env python
import pika
from message_queue_handlers.PrintQueuePublisher import PrintQueuePublisher
from message_queue_handlers.EmailEventQueueConsumer import EmailEventQueueConsumer
from repository.EmailEventRepository import EmailEventRepository
from parsers.EmailEventToJsonParser import EmailEventToJsonParser
from db.EngineFactory import SessionFactory
from parsers.ByteArrayToDictParser import ByteArrayToDictParser
from parsers.DictToEmailEventParser import DictToEmailEventParser
from validators.EmailEventValidator import EmailEventsValidator

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    session = SessionFactory().create()
    emailRepository = EmailEventRepository(session)

    byteArrayToDictParser = ByteArrayToDictParser()
    dictToEmailEventParser = DictToEmailEventParser()
    emailEventToJsonParser = EmailEventToJsonParser()
    emailEventsValidator = EmailEventsValidator()
    printQueuePublisher = PrintQueuePublisher(channel)
    emailEventQueueConsumer = EmailEventQueueConsumer(channel, emailRepository, byteArrayToDictParser, dictToEmailEventParser, 
                                                    emailEventToJsonParser, emailEventsValidator, printQueuePublisher)
    emailEventQueueConsumer.set_consumer()
    printQueuePublisher.set_publisher()

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()