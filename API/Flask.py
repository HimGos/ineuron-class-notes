# TODO: API is just a set of rules.
# TODO: POST means sending a data in BODY , while GET means sending data in URL.

from flask import Flask, request, jsonify

# Step 1 - Creating object of Flask class
app = Flask(__name__)


# Step 2 -  setting route and method
@app.route('/abc', methods=['GET', 'POST'])     # @ is annotation. It means whatever function is after this line, execute it. Route is a function of Flask class.
def test1():
    if (request.method == 'POST'):              # request is also a class. Defining we want data in POST method.
        a = request.json['num1']                # Taking data in json format and assigning 'a' variable.
        b = request.json['num2']                # num1 & num2 are keys of json.
        result = a+b
        return jsonify((str(result)))           # Asking to jsonify the result


@app.route('/himz', methods=['GET', 'POST'])         # Now Route name is different, so API also changed. Only test2 will be executed.
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify(result)


@app.route('/test', methods=['GET', 'POST'])         # Now Route name is different, so API also changed. Only test3 will be executed.
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify(result)


# I can access function becoz route is defined right over it. Same function names give compile time error.

if __name__ == '__main__':
    app.run()                                  # Run function of FLASK class is needed to execute the program.


# TODO: http://127.0.0.1:5000/ is the output where 5000 is port number and other number is local host IP
# In postman or other software I need to paste this url and place the route name behind it.
