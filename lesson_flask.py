import csv
import datetime
import json
import random
import string

import os
import requests
import sqlite3

from flask import Flask, make_response
from flask import request



# app = Flask('app')
print(__name__)
app = Flask(__name__)



####################
@app.route('/')
def hello():
    return 'Hello'



####################
@app.route('/now')
def now():
    return str(datetime.datetime.now())


"""
TypeError: The view function did not return a valid response. 
The return type must be a string, dict, list, tuple with headers or status, 
Response instance, or WSGI callable, but it was a datetime.
"""



####################
"""
@app.route('/get-requirements')
def get_requirements():
    try:
        f = open('requirements.txt', 'r') 
        # ...
        # <--- exception
    except Exception as ex:
        pass
    finally:
        f.close()
"""

@app.route('/get-requirements')
def get_requirements():
    # with open('requirements.txt', 'r') as f:
    #     result = f.read()
    # print(result, type(result))
    # result = result.replace('\n', '<br>')
    # print(result)
    # return result
    with open('requirements.txt', 'r') as f:
        reader = csv.DictReader(f)
        print(reader, type(reader))  # <csv.DictReader object at 0x7f301b46fa30> <class 'csv.DictReader'>
        rows = [row for row in reader]
    # str_rows = '<br>'.join([
    #     str(record)
    #     for record in rows
    # ])
    # return str_rows
    print(rows)  # [{'certifi==2022.9.24': 'charset-normalizer==2.1.1'}, {'certifi==2022.9.24': 'click==8.1.3'},...
    print(type(rows))  # <class 'list'>
    return str(rows)



###################
@app.route('/get-astronauts')
def get_astronauts():
    response = requests.get('http://api.open-notify.org/astros.json')
    print(response, type(response))  # <Response [200]> <class 'requests.models.Response'>
    if response.status_code == 200:
        # text = response.content
        print(response.content)  # b'{"message": "success", "people": [{"name": "Kjell Lindgren", "craft": "ISS"}, {"name":...
        print(type(response.content))  # <class 'bytes'>
        print(response.text)  # {"message": "success", "people": [{"name": "Kjell Lindgren", "craft": "ISS"}, {"name":...
        print(type(response.text))  # <class 'str'>
        resp = json.loads(response.text)
        print(resp)  # {'message': 'success', 'people': [{'name': 'Kjell Lindgren', 'craft': 'ISS'}, {'name':...
        print(type(resp))  # <class 'dict'>
        return f'Austranauts number: {resp["number"]}'
        # return f'Austranauts number: {resp.get("number", '<N/A>')}'
    else:
        return f'Error {response.status_code}'



###################
# @app.route('/gen_password')
# def gen_password():
#     return ''.join([
#         random.choice(string.ascii_lowercase)
#         for _ in range(10)
#     ])
###################
@app.route('/gen-password')  # http://127.0.0.1:5000/gen-password?length=19&digit=1&specials=1
def gen_password():
    # """ If argument HTTP request --- length --- obiazatelnyy my hotim"""
    # if 'length' not in request.args:
    #     return make_response('Missing argument "length", 400')
    # length = int(request.args['length'])
    DEFAULT_LENGTH = 10
    length = int(request.args.get('length', DEFAULT_LENGTH))
    # return ''.join([
    #     random.choice(string.ascii_lowercase)
    #     for _ in range(length)
    # ])
    digits = int(request.args.get('digit', 0))
    specials = int(request.args.get('specials', 0))

    generation_symbols = string.ascii_lowercase
    if digits == 1:
        generation_symbols += string.digits
    if specials == 1:
        generation_symbols += '!@#$%^&*('

    print(generation_symbols)  # abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(
    return ''.join([
        random.choice(generation_symbols)
        for _ in range(length)
    ])



####################
@app.route('/get-customers')
def get_customer():
    query = 'SELECT FirstName, LastName FROM customers WHERE City = "Oslo" or City = "Paris"'
    records = execute_query(query)
    print(records, type(records))  # [('Bjørn', 'Hansen'), ('Camille', 'Bernard'), ('Dominique', 'Lefebvre')] <class 'list'>
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return result
######################
"""
def execute_query(query):
    # db_path = '/home/yshost/PycharmProjects/test_project/chinook.db'
    # db_path = os.getcwd() + '/chinook.db'
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records
"""

"""
def foo(*args):
    print(type(args), args)
"""

"""
def bar(a, b):
    return a + b
    
def foo(*args):
    print(type(args), args)
    for i in args:
        print(i)
    print(bar(*args))   # !!! if bar(args) ---> mistake: args - 1 argument tuple
"""

def execute_query(query, *args):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    print(conn)  # <sqlite3.Connection object at 0x7f03a699fc60>
    cur = conn.cursor()
    print(cur)  # <sqlite3.Cursor object at 0x7f03a68ced50>
    print(args, type(args))
    cur.execute(query, args)   # tut  args  -- tuple  !!!!
    print(cur)  # <sqlite3.Cursor object at 0x7f03a68ced50>
    records = cur.fetchall()  # list of tuples !!!
    print(records, type(records))  # [('Bjørn', 'Hansen'), ('Camille', 'Bernard'), ('Dominique', 'Lefebvre')] <class 'list'>
    return records



####################################
@app.route('/get-customers-st-bad')
def get_customer_st():
    state = request.args.get('state', '')
    print(state)  # CA" UNION ALL select BillingAddress, Total from invoices --
    query = f'SELECT FirstName, LastName FROM customers WHERE State = "{state}"'  # <--- bad solving,
    print(query)  # SELECT FirstName, LastName FROM customers WHERE State = "CA" UNION ALL select BillingAddress, Total from invoices --"
    # http://localhost:5000/get-customers-st-bad?state=CA" UNION ALL select BillingAddress, Total from invoices --
    # http://localhost:5000//get-customers-st-bad?state=CA%22%20UNION%20ALL%20select%20BillingAddress,%20Total%20from%20invoices%20--

    # !!! sql in'ektsiya !!!
    records = execute_query(query)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return result


@app.route('/get-customers-st-good')
def get_customers():
    state = request.args.get('state', '')
    print(state)
    query = 'SELECT FirstName, LastName FROM customers WHERE State = ?'
    print(query)  # SELECT FirstName, LastName FROM customers WHERE State = ?
    records = execute_query(query, state)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return result

# Примечание 1: В PostgreSQL (UPD: и в MySQL) вместо знака '?' для подстановки используется: %s


#######################
@app.route('/get-revenue')
def get_revenue():
    query = 'SELECT sum(UnitPrice*Quantity) FROM invoice_items'
    records = execute_query(query)
    # result = '<br>'.join([
    #     str(record)
    #     for record in records
    # ])
    print(records, type(records))  # [(2328.599999999957,)] <class 'list'>
    result = str(records[0][0])  # records here is 1 element(len=1) so use without join !!!!!
    return result



# app.run(debug=True)
# app.run(host="localhost", port=8080, debug=True)
app.run(host="localhost", port=5000, debug=True)
