# MathAPI

![mathapi](https://github.com/user-attachments/assets/877339fd-7ce7-4b61-81aa-34bb5a91f2a9)

MathAPI is a simple Flask-based API that provides various mathematical functions, constants, unit conversions, and basic arithmetic operations.

## Endpoints

### Home
- **`GET /`**
  - Returns a welcome message and a list of available endpoints.

### Mathematical Functions
- **`GET /math/<function>?v=number`**
  - Computes mathematical functions.
  - Supported functions:
    - `sin`, `cos`, `tan` (for angles in degrees)
    - `sqrt`, `log`, `log10`
    - `factorial`, `ceil`, `floor`
  - Example: `/math/sin?v=30`
  
- **`GET /math/radians/<function>?v=number`**
  - Computes trigonometric functions with input in radians.
  - Supported functions:
    - `sin`, `cos`, `tan`
  - Example: `/math/radians/sin?v=0.5235987756`

- **`GET /math/exp?base=number&exponent=number`**
  - Computes exponentiation.
  - Example: `/math/exp?base=2&exponent=3`

- **`GET /math/mod?num1=number&num2=number`**
  - Computes modulus.
  - Example: `/math/mod?num1=10&num2=3`

- **`GET /math/is_prime?n=number`**
  - Checks if a number is prime.
  - Example: `/math/is_prime?n=7`

- **`GET /math/fibonacci?n=number`**
  - Generates Fibonacci sequence up to n numbers.
  - Example: `/math/fibonacci?n=10`

### Constants
- **`GET /constants`**
  - Retrieves important mathematical constants.
  - Returns:
    - `pi` (π)
    - `e` (Euler's number)
    - `golden_ratio`
    - `silver_ratio`
    - `planck_constant`
    - `avogadro_number`
    - `speed_of_light`
    - `gravitational_constant`
    - `boltzmann_constant`
    - `gas_constant`
    - `elementary_charge`

### Unit Conversion
- **`POST /convert`**
  - Converts between units.
  - Currently supports:
    - Celsius ↔ Fahrenheit
    - Celsius ↔ Kelvin
    - Meters ↔ Kilometers
    - Meters ↔ Centimeters
    - Inches ↔ Centimeters
    - Feet ↔ Meters
    - Yards ↔ Meters
    - Miles ↔ Kilometers
    - Kilograms ↔ Pounds
  - Example:
    ```json
    {
      "v": 100,
      "from": "c",
      "to": "f"
    }
    ```

### Basic Arithmetic Operations
- **`POST /calculate`**
  - Performs basic arithmetic operations.
  - Requires JSON input with `num1`, `num2`, and `operation`.
  - Supported operations:
    - `add`, `subtract`, `multiply`, `divide`
  - Example:
    ```json
    {
      "num1": 10,
      "num2": 5,
      "operation": "add"
    }
    ```

## Running the project locally 

1. Install the required dependencies:
```sh
pip install flask
```

2. Run the Flask application:
```sh
python main.py
```

3. Access the API at
`http://127.0.0.1:5000/`
