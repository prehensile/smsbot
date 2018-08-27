import logging

from flask import Flask, request

import bothandler
import nexmohandler


bot_handler = bothandler.BotHandler()
sms_handler = nexmohandler.NexmoHandler()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/sms/receive')
def api_sms_receive():
    parsed = sms_handler.parse_request( request.values )
    messages = bot_handler.handle( parsed['message'] )
    for message_out in messages:
        r = sms_handler.send_message(
            to_number = parsed['originating_number'],
            message = message_out, 
            from_name = parsed['receiving_number']
        )
        logging.info( r )
    return "OK!"