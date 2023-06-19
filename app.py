from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')

    return "Hello QuyTN7! Welcome to Capstone Udacity"

if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port=80)