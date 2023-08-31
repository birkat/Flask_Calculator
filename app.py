from flask import Flask, request

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
        result = int(number1) + int(number2)
    elif operations == "multiply":
        result = int(number1) * int(number2)
    elif operations == "division":
        result = int(number1) / int(number2)
    else:
        result = int(number1) - int(number2)
    return f"The operations is {operations} and the result is {result}"


print(__name__)

if __name__ == '__main__':
    obj.run(debug=True)