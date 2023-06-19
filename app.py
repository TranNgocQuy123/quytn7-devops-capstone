from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello QuyTN7! Welcome to Capstone Udacity"

if __name__ == "__main__":
    ## stream logs to a file
    app.run(host='0.0.0.0', port=80, debug=True)  