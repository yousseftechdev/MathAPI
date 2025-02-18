from flask import Flask, request, jsonify
from math import sin, cos, tan, radians, pi, e, sqrt, log, log10, factorial, ceil, floor

app = Flask(__name__)

@app.route("/")
def home():
    return ("<h1>Hey! This is my first API, welcome to my home page</h1>"
            "<h2>Yes, I know this is completely useless as most of this functionality can be implemented with no api but I thought this would make a great first API, just like how every programmer starts off with a calculator project</h2>"
            "<br><h2>MathAPI</h2>"
            "<p>Available Endpoints:</p>"
            "<ul>"
            "<li><b>/math/&lt;function&gt;?v=number</b> - Compute mathematical functions (sin, cos, tan for angles in degrees, sqrt, log, log10, factorial, ceil, floor).</li>"
            "<li><b>/constants</b> - Retrieve important mathematical constants like π (pi), e (Euler's number), and the golden ratio.</li>"
            "<li><b>/convert?v=num&from=unit1&to=unit2</b> - Convert between units (currently supports Celsius ↔ Fahrenheit).</li>"
            "<li><b>/calculate</b> (POST) - Perform basic arithmetic operations (add, subtract, multiply, divide). Requires JSON input with 'num1', 'num2', and 'operation'.</li>"
            "</ul>")

@app.route("/math/<function>")
def math(function):
    try:
        value = float(request.args.get('v'))
        
        if function in ['sin', 'cos', 'tan']:
            value = radians(value)
        
        if function == 'sin':
            return jsonify({'result': sin(value)})
        elif function == 'cos':
            return jsonify({'result': cos(value)})
        elif function == 'tan':
            return jsonify({'result': tan(value)})
        elif function == 'sqrt':
            return jsonify({'result': sqrt(value)})
        elif function == 'log':
            return jsonify({'result': log(value)})
        elif function == 'log10':
            return jsonify({'result': log10(value)})
        elif function == 'factorial':
            if value < 0 or not value.is_integer():
                return jsonify({'error': 'Factorial is only defined for non-negative integers'}), 400
            return jsonify({'result': factorial(int(value))})
        elif function == 'ceil':
            return jsonify({'result': ceil(value)})
        elif function == 'floor':
            return jsonify({'result': floor(value)})
        else:
            return jsonify({'error': 'Invalid function'}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing value parameter'}), 400

@app.route("/constants")
def constants():
    return jsonify({
        'pi': pi,
        'e': e,
        'golden_ratio': (1 + 5 ** 0.5) / 2,
        'silver_ratio': 1 + 2 ** 0.5,
        'planck_constant': 6.62607015e-34,
        'avogadro_number': 6.02214076e23,
        'speed_of_light': 299792458  # in meters per second
    })

@app.route("/convert")
def convert():
    try:
        value = float(request.args.get('v'))
        from_unit = request.args.get('from').lower()
        to_unit = request.args.get('to').lower()
        
        if from_unit == "c" and to_unit == "f":
            return jsonify({'result': (value * 9/5) + 32})
        elif from_unit == "f" and to_unit == "c":
            return jsonify({'result': (value - 32) * 5/9})
        else:
            return jsonify({'error': 'Unsupported conversion'}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation')
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

if __name__ == '__main__':
    app.run(debug=True)
