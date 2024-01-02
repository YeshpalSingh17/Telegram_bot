import os
from bot import bot 

def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        update = bot.updates_handler.process_new_updates([Update.de_json(environ["wsgi.input"].read())])[0]
        return ""
    else:
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b"Hello World"]