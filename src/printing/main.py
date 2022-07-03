#!/usr/bin/env python
import pika
import _thread

from parsers.ByteArrayToDictParser import ByteArrayToDictParser
from parsers.CacheToHtmlParser import CacheToHtmlParser
from message_queue_handlers.PrintQueuePublisher import PrintQueuePublisher
from websocket.websocket import Websocket

if __name__ == "__main__":
    dummy_cache = []
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    cacheToHtmlParser = CacheToHtmlParser()
    byteArrayToDictParser = ByteArrayToDictParser()
    websocket = Websocket(dummy_cache, cacheToHtmlParser)
    printQueuePublisher = PrintQueuePublisher(channel, byteArrayToDictParser, dummy_cache)

    printQueuePublisher.set_consumer()

    print(' [*] Waiting for messages. To exit press CTRL+C')
    _thread.start_new(channel.start_consuming, ())
    websocket.run()