#!/usr/bin/env python

import click
import json
from flask import Flask, request


# Init with default config
app = Flask(__name__)
HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'content-type': 'application/json; charset=utf-8'
}


@click.command()
@click.option('--port', default=8888, metavar='<portNum>', show_default=True)
@click.option('--debug', default=False, is_flag=True, metavar='')
def run(port, debug):
    """
    Entry point to execute script (runs the web server)
    """
    return init_api(port, debug)


def init_api(port=8888, debug=False):
    """
    Runs web server
    """
    app.logger.info("Starting api with config: " + str(app.config))
    app.run(host='0.0.0.0', port=port, debug=debug, threaded=True)


@app.route("/")
def ask():
    text = request.args.get('text', '<default-text>')
    response = {
        "status": "ok",
        "input": request.args,
        "text-input": text,
        "output": "All Good :)"
    }
    return (json.dumps(response), 200, HEADERS)

if __name__ == '__main__':
    run()
