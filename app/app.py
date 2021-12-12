"""Web Application Program"""
from flask import Flask, render_template, request, flash
from calc.calculator import Calculator

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def homepage():
    """Display homepage"""
    return render_template('index.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    # pylint: disable=no-else-return
    """Display the form"""

    if request.method == 'POST':
        # Clear the table if the user requested to
        if request.form.get('action') == 'Clear':
            Calculator.clear_csv_files()
            flash("Table is cleared!", "success")
            return render_template('result.html', value1="None",
                                   value2="None", operation="None", result="None")

        # variables
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        result = ""

        # Throw an error for entering empty values
        if value1 == "" or value2 == "":
            flash("Input Empty Error!", "error")
            # Get calculator history
            Calculator.read_csv_file()
            items = Calculator.get_history()
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation,
                                   items=items, result="")

        getattr(Calculator, operation)(value1, (value2,))

        # Check for division by zero
        if Calculator.get_last_calculation() is None:
            flash("Division by Zero Error!", "error")
            result = str(Calculator.get_last_calculation())
            Calculator.put_history_to_csv(operation, value1, value2, result)
            Calculator.read_csv_file()
            items = Calculator.get_history()
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation,
                                   items=items, result=result)
        else:
            flash("Success!", "success")
            result = str(Calculator.get_last_calculation())
            Calculator.put_history_to_csv(operation, value1, value2, result)
            Calculator.read_csv_file()
            items = Calculator.get_history()
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation,
                                   items=items, result=result)
    else:
        return render_template('form.html')
