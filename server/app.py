#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# /Flask application in flask_app.py has a resource available at "/"
# /Flask application in flask_app.py displays "Python Operations with Flask Routing and Views" in h1 in browser.
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# /Flask application in flask_app.py has a resource available at "/print/<parameter>"
# /Flask application in flask_app.py displays text of route in browser.
# /Flask application in flask_app.py displays text of route in console.
@app.route('/print/<string:parameter>')
def print_route(parameter):
    print(f'{parameter}')
    return f'{parameter}'


# /Flask application in flask_app.py has a resource available at "/count/<parameter>".
# /Flask application in flask_app.py counts through range of parameter in "/count/<parameter" on separate lines.   
@app.route('/count/<int:parameter>')  
def count(parameter):
    result = ''
    for i in range(parameter):
        result += f'{i}\n'
    return result


# /Flask application in flask_app.py has a resource available at "/math/<parameters>".
# /Flask application in flask_app.py adds parameters in "/math/" resource when operation is "+".
# /Flask application in flask_app.py subtracts parameters in "/math/" resource when operation is "-".
# /Flask application in flask_app.py multiplies parameters in "/math/" resource when operation is "*".
# /Flask application in flask_app.py divides parameters in "/math/" resource when operation is "div".
# /Flask application in flask_app.py finds remainder of parameters in "/math/" resource when operation is "%"
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)

    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
