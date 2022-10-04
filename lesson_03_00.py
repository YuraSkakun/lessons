import datetime
import random
import string

from flask import Flask

app = Flask('app')


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


app.run()
