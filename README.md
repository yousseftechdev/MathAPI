# MathAPI

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

### Constants
- **`GET /constants`**
  - Retrieves important mathematical constants.
  - Returns:
    - `pi` (π)
    - `e` (Euler's number)
    - `golden_ratio`

### Unit Conversion
- **`GET /convert?v=num&from=unit1&to=unit2`**
  - Converts between units.
  - Currently supports:
    - Celsius ↔ Fahrenheit
  - Example: `/convert?v=100&from=c&to=f`

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