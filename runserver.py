import os
from flask import Flask
import unittest

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return app.send_static_file('client.html')

class User (unittest.TestCase):
    name =  "Prueba_test"
    id = "123_test"
    email = "test@gmail.es"

    def get_name_test(self):
        self.assertEqual(self.name, "Prueba_test")

        return self.name

    def get_id_test(self):
        self.assertEqual(self.id, "123_test")

        return self.id

    def get_email_test(self):
        self.assertEqual(self.email,"test@gmail.es")

        return self.email

    def login_test(self,id="123_test",password="123456"):
        self.assertEqual(id,"123_test")
        self.assertEqual(password,"123456")

        return True

    def get_gender_test(self):
        gender = "male"

        self.assertEqual(gender,"male")

        return gender


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
