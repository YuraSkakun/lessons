import datetime
import json
import os
import random
import string
import requests

from flask import Flask
from flask import request
from faker import Faker

print("hello")
app = Flask('app')

# Constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(__file__)
print(os.path.abspath(__file__))
print(ROOT_DIR)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/now')
def now():
    return str(datetime.datetime.now())


@app.route('/gen_password')
def gen_password():
    return ''.join([
        random.choice(string.ascii_lowercase)
        for _ in range(10)
    ])


#  use in route: http://127.0.0.1:5000/gen_password_new?length=10
@app.errorhandler(400)
def handle_bad_request(error):
    return("Please provide the required length of the password by adding ?length=N " \
          "parameter in the URL, where N is equal to the number of required length")


@app.route('/gen_password_new')
def gen_password_new():
    print(request)  # <Request 'http://127.0.0.1:5000/gen_password_new?length=10' [GET]>
    print(request.args)  #ImmutableMultiDict([('length', '10')])
    length = request.args['length']
    # length = request.args.get('length')
    # length = request.args.get('length', 9)  #10 <class 'str'>
    print(length, type(length))  #10 <class 'str'>
    try:
        val = int(length)
        if (val > 0):
            if (8 <= val <= 24):
                return ''.join(
                    [
                        random.choice(string.ascii_lowercase)
                        for _ in range(val)
                    ]
                )
            else:
                return "Length should be in the range from 8 to 24."
        else:
            return "Length should be bigger than 0."
    except ValueError:
        return ("Length should be a number!")


@app.route('/read_requirements')
def read_requirements():
    file_path = ROOT_DIR + '/requirements.txt'
    print(file_path, type(file_path))
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(file_contents, type(file_contents))
        result_string = ''.join(file_contents)
        print('###')
        print(result_string)
    return result_string


@app.route('/100-random-users')
def random_users():
    fake = Faker()
    result_string = "\n".join([
        fake.name() + ' ' + fake.email()
        for _ in range(100)
    ])
    return str(result_string)


@app.route('/get_astronauts')
def get_astronauts():
    response = requests.get('http://api.open-notify.org/astros.json')
    if response.status_code == 200:
        resp = json.loads(response.content)
        return f"Astronauts number: {resp['number']}"
    else:
        return f"Error code is: {response.status_code}"


app.run()
