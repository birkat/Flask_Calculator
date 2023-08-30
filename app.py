from flask import Flask, request, render_template

obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to Flask"

@obj.route('/cal', methods = ['GET'])
def math_operations():
    operations = request.json["operations"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operations == "add":
        result = number1 + number2
    elif operations == "multiply":
        result = number1 * number2
    elif operations == "division":
        result = number1 / number2
    else:
        result = number1 - number2
    return result


print(__name__)

if __name__ == '__main__':
    obj.run(debug=True)