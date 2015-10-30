from flask import Flask
import unittest

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World 2!"

class Usuario(unittest.TestCase):
    def get_email(self):
        assert 5>2


if __name__ == "__main__":
    app.run()
