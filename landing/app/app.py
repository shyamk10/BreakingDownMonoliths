from flask import Flask, render_template, request, flash, redirect, url_for
import json
import requests

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    response = requests.get('http://add-service:5050/' + n1 + '/' + n2)
    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def minus(n1, n2):
    response = requests.get('http://minus-service:5050/' + n1 + '/' + n2)
    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def multiply(n1, n2):
    response = requests.get('http://multiply-service:5050/' + n1 + '/' + n2)
    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def divide(n1, n2):
    response = requests.get('http://divide-service:5050/' + n1 + '/' + n2)
    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def lcm(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        response = requests.get('http://lcm-service:5050/' + str(n1) + '/' + str(n2))
        result = json.loads(response.content.decode('utf-8'))
        return result['result']
    else:
        raise ValueError('Inputs must be integers.')


def hcf(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        response = requests.get('http://hcf-service:5050/' + str(n1) + '/' + str(n2))
        result = json.loads(response.content.decode('utf-8'))
        return result['result']
    else:
        raise ValueError('Inputs must be integers.')


def modulus(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        response = requests.get('http://modulus-service:5050/' + str(n1) + '/' + str(n2))
        result = json.loads(response.content.decode('utf-8'))
        return result['result']
    else:
        raise ValueError('Inputs must be integers.')


@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        req1 = request.form['first']
        req2 = request.form['second']
        number_1 = float(req1)
        number_2 = float(req2)
    except ValueError:
        flash('Invalid input. Please enter numbers only.')
        return redirect(url_for('index'))
    except KeyError:
        number_1 = None
        number_2 = None
    operation = request.form.get('operation')
    result = 0
    try:
        if operation == 'add':
            result = add(str(number_1), str(number_2))
        elif operation == 'minus':
            result = minus(str(number_1), str(number_2))
        elif operation == 'multiply':
            result = multiply(str(number_1), str(number_2))
        elif operation == 'divide':
            try:
                if number_2 == 0:
                    raise ZeroDivisionError('Cannot divide by zero.')
                else:
                    result = divide(str(number_1), str(number_2))
            except ZeroDivisionError:
                flash('Can not divide by 0')
        elif operation == 'hcf':
            try:
                if int(number_1) == number_1 and int(number_2) == number_2:
                    result = hcf(int(number_1), int(number_2))
                else:
                    raise ValueError('Inputs must be integers.')
            except ValueError:
                flash('Invalid input. Please enter integer numbers only.')
        elif operation == 'lcm':
            try:
                if int(number_1) == number_1 and int(number_2) == number_2:
                    result = lcm(int(number_1), int(number_2))
                else:
                    raise ValueError('Inputs must be integers.')
            except ValueError:
                flash('Invalid input. Please enter integer numbers only.')
        elif operation == 'modulus':
            try:
                if int(number_1) == number_1 and int(number_2) == number_2:
                    result = modulus(int(number_1), int(number_2))
                else:
                    raise ValueError('Inputs must be integers.')
            except ValueError:
                flash('Invalid input. Please enter integer numbers only.')

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    except ValueError:
        print('cant convert', req1, req2, 'to int')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
