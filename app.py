from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            result = f"The sum of {num1} and {num2} is {num1 + num2}"
        elif ops == 'subtract':
            result = f"The subtraction of {num1} and {num2} is {num1 - num2}"
        elif ops == 'multiply':
            result = f"The multiplication of {num1} and {num2} is {num1 * num2}"
        elif ops == 'divide':
            if num2 == 0:
                result = "Error: Division by zero is not allowed."
            else:
                result = f"The division of {num1} and {num2} is {num1 / num2}"
        else:
            result = "Error: Invalid operation"

        return render_template('results.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
