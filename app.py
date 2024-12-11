from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def things():
    return jsonify({"foo"})

if __name__ == '__main__':
    app.run()



