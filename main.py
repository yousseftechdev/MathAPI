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
            "<li><b>/math/radians/&lt;function&gt;?v=number</b> - Compute trigonometric functions (sin, cos, tan) with input in radians.</li>"
            "<li><b>/math/exp?base=number&exponent=number</b> - Compute exponentiation.</li>"
            "<li><b>/math/mod?num1=number&num2=number</b> - Compute modulus.</li>"
            "<li><b>/math/is_prime?n=number</b> - Check if a number is prime.</li>"
            "<li><b>/math/fibonacci?n=number</b> - Generate Fibonacci sequence up to n numbers.</li>"
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

@app.route("/math/radians/<function>")
def math_radians(function):
    try:
        value = float(request.args.get('v'))
        
        if function == 'sin':
            return jsonify({'result': sin(value)})
        elif function == 'cos':
            return jsonify({'result': cos(value)})
        elif function == 'tan':
            return jsonify({'result': tan(value)})
        else:
            return jsonify({'error': 'Invalid function'}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing value parameter'}), 400

@app.route("/math/exp")
def exp():
    try:
        base = float(request.args.get('base'))
        exponent = float(request.args.get('exponent'))
        return jsonify({'result': base ** exponent})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

@app.route("/math/mod")
def mod():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({'result': num1 % num2})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

@app.route("/math/is_prime")
def is_prime():
    try:
        num = int(request.args.get('n'))
        if num < 2:
            return jsonify({'result': False})
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return jsonify({'result': False})
        return jsonify({'result': True})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

@app.route("/math/fibonacci")
def fibonacci():
    try:
        n = int(request.args.get('n'))
        if n < 0:
            return jsonify({'error': 'Invalid parameter'}), 400
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return jsonify({'result': fib_sequence[:n]})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

@app.route("/constants")
def constants():
    return jsonify({
        'pi': pi,
        'e': e,
        'golden_ratio': (1 + 5 ** 0.5) / 2,
        'silver_ratio': 1 + 2 ** 0.5,
        'planck_constant': 6.62607015e-34,
        'avogadro_number': 6.02214076e23,
        'speed_of_light': 299792458,
        'gravitational_constant': 6.67430e-11,
        'boltzmann_constant': 1.380649e-23,
        'gas_constant': 8.314462618,
        'elementary_charge': 1.602176634e-19
    })

@app.route("/convert", methods=['POST'])
def convert():
    try:
        data = request.get_json()
        value = float(data.get('v'))
        from_unit = data.get('from').lower()
        to_unit = data.get('to').lower()    
        
        if from_unit == "c" and to_unit == "f":
            return jsonify({'result': (value * 9/5) + 32})
        elif from_unit == "f" and to_unit == "c":
            return jsonify({'result': (value - 32) * 5/9})
        elif from_unit == "c" and to_unit == "k":
            return jsonify({'result': value + 273.15})
        elif from_unit == "k" and to_unit == "c":
            return jsonify({'result': value - 273.15})
        
        elif from_unit == "m" and to_unit == "km":
            return jsonify({'result': value / 1000})
        elif from_unit == "km" and to_unit == "m":
            return jsonify({'result': value * 1000})
        elif from_unit == "m" and to_unit == "cm":
            return jsonify({'result': value * 100})
        elif from_unit == "cm" and to_unit == "m":
            return jsonify({'result': value / 100})
        elif from_unit == "in" and to_unit == "cm":
            return jsonify({'result': value * 2.54})
        elif from_unit == "cm" and to_unit == "in":
            return jsonify({'result': value / 2.54})
        elif from_unit == "ft" and to_unit == "m":
            return jsonify({'result': value * 0.3048})
        elif from_unit == "m" and to_unit == "ft":
            return jsonify({'result': value / 0.3048})
        elif from_unit == "yd" and to_unit == "m":
            return jsonify({'result': value * 0.9144})
        elif from_unit == "m" and to_unit == "yd":
            return jsonify({'result': value / 0.9144})
        elif from_unit == "mi" and to_unit == "km":
            return jsonify({'result': value * 1.60934})
        elif from_unit == "km" and to_unit == "mi":
            return jsonify({'result': value / 1.60934})
        
        elif from_unit == "kg" and to_unit == "lb":
            return jsonify({'result': value * 2.20462})
        elif from_unit == "lb" and to_unit == "kg":
            return jsonify({'result': value / 2.20462})
        
        else:
            return jsonify({'error': 'Unsupported conversion'}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid or missing parameters'}), 400

@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation')

        if num1 is None or num2 is None or operation is None:
            return jsonify({'error': 'Missing parameters'}), 400

        num1 = float(num1)
        num2 = float(num2)

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
    except (TypeError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
