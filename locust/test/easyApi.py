# -*- coding=utf-8 -*-

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/hello", methods=["POST", "GET"])
def hello():
    return jsonify({
        "1": "hello"
    })


if __name__ == '__main__':
    app.run(debug=False)
