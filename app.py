#!/usr/bin/env python
from flask import Flask

# Init with default config
app = Flask(__name__)
app.config.update(dict(
    headers={
        'Access-Control-Allow-Origin': '*',
        'content-type': 'application/json; charset=utf-8'
    }
))


def run():
    """
    Entry point to execute script
    Forwards call to run web sever
    """
    return init_api()


def init_api(port=8888, debug=False):
    """
    Runs web server
    """
    app.logger.info("Starting api with config: " + str(app.config))
    app.run(host='0.0.0.0', port=port, debug=debug, threaded=True)

if __name__ == '__main__':
    run()
