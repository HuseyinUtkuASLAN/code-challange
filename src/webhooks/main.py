#!/usr/bin/env python
from flask import Flask, request
from ResponseFactory import ResponseFactory
from message_queue_handlers.EmailEventQueueHandler import EmailEventQueueHandler
from models.Adapter.FormToEmailEventParser import FormToEmailEventParser

app = Flask(__name__)


@app.route('/webhooks', methods = ['POST'])
def webhooks():
    email_event = FormToEmailEventParser().Map(request.get_json())
    
    emailEvenHandlerQueue.publish(email_event)
    
    return ResponseFactory().create()


if __name__ == '__main__':
    
    emailEvenHandlerQueue = EmailEventQueueHandler()
    emailEvenHandlerQueue.Init()

    app.run(host='0.0.0.0', port=5000)
