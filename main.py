from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

if (__name__=='__main__'):
    app.run()


