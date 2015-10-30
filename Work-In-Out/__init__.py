
import random
from flask import Flask
app = Flask(__name__, static_url_path='')


usuarios ={}

@app.route('/')
def root():
    return app.send_static_file('client.html')

@app.route('/sign_in', methods=['POST'])
def sign_in():
    registro = random.random()

    if (registro not in usuarios):
        return registro
    else:
        return False

@app.route('/sign_up', methods=['POST'])
def sign_up():
    return 'Te has registrado!'

@app.route('/sign_out', methods=['POST'])
def sign_out():
    return 'Has salido!'