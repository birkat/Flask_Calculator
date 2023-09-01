from flask import Flask, request, render_template, url_for, redirect

obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to Flask"

@obj.route('/cal', methods = ['GET', 'POST'])
def math_operations():
    if request.method == "GET":
        return render_template('result.html')
        # operations = request.form["operations"]
        # number1 = request.form["number1"]
        # number2 = request.form["number2"]
    else:
        operations = request.form["operations"]
        number1 = request.form["number1"]
        number2 = request.form["number2"]

        if operations == "add":
            result = int(number1) + int(number2)
        elif operations == "multiply":
            result = int(number1) * int(number2)
        elif operations == "division":
            result = int(number1) / int(number2)
        else:
            result = int(number1) - int(number2)
        return f"The operations is {operations} and the result is {result}"
        #return redirect(url_for(result,str(result)))


print(__name__)

if __name__ == '__main__':
    obj.run(debug=True)