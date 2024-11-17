"""
Simple Calculator application that takes
two parameters and returns the result of
- addition
- subtraction
- multiplication
- division
- floor
- mod
- power
- root
"""

from flask import Flask, request
app = Flask(__name__)


def message(op: str, arg1: int, arg2: int):
    """Returns message to be printed on page

    Parameters:
    op (str): Mathematical operation
    arg1 (int): Argument 1
    arg2 (int): Argument 2

    Returns:
    str

   """
    mes: str
    match op:
        case 'add':
            mes = f"<h1>{arg1} + {arg2} = {arg1 + arg2}</h1>"
        case 'subtract':
            mes = f"<h1>{arg1} - {arg2} = {arg1 - arg2}</h1>"
        case 'multiply':
            mes = f"<h1>{arg1} * {arg2} = {arg1 * arg2}</h1>"
        case 'divide':
            mes = f"<h1>{arg1} / {arg2} = {arg1 / arg2}</h1>"
        case 'floor':
            mes = f"<h1>{arg1} // {arg2} = {arg1 // arg2}</h1>"
        case 'mod':
            mes = f"<h1>{arg1} % {arg2} = {arg1 % arg2}</h1>"
        case 'pow':
            mes = f"<h1>{arg1}^{arg2} = {arg1 ** arg2}</h1>"
        case 'root':
            mes = f"<h1>{arg1}^(1/{arg2}) = {arg1 ** (1 / arg2)}</h1>"
        case _:
            mes = "<h1>Invalid input</h1>"
    return mes

@app.route('/calculate')
def calculate():  # put application's code here
    """Prints message on page based on parameters

    Parameters:
    op (str): Mathematical operation
    arg1 (int): Argument 1
    arg2 (int): Argument 2

    Returns:
    str

   """
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    return message(op, arg1, arg2)

if __name__ == '__main__':
    app.run()
