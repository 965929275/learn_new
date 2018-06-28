# encoding:utf8
from flask import Flask,request
from  xmlrpclib import ServerProxy
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/toutiao', methods=['POST'])
def spider():
    url = request.json.get('url')
    server = ServerProxy("http://localhost:8088")


    words = server.run(url)

    print (words)
    return words


if __name__ == "__main__":
    app.run(debug=True)