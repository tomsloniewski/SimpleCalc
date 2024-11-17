from unittest import case

from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def calculate():  # put application's code here
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    match op:
        case 'add':
            return f"<h1>{arg1} + {arg2} = {arg1+arg2}</h1>"
        case 'subtract':
            return f"<h1>{arg1} - {arg2} = {arg1-arg2}</h1>"
        case 'multiply':
            return f"<h1>{arg1} * {arg2} = {arg1*arg2}</h1>"
        case 'divide':
            return f"<h1>{arg1} / {arg2} = {arg1/arg2}</h1>"
        case 'floor':
            return f"<h1>{arg1} // {arg2} = {arg1//arg2}</h1>"
        case 'mod':
            return f"<h1>{arg1} % {arg2} = {arg1%arg2}</h1>"
        case 'pow':
            return f"<h1>{arg1}^{arg2} = {arg1**arg2}</h1>"
        case 'root':
            return f"<h1>{arg1}^(1/{arg2}) = {arg1**(1/arg2)}</h1>"
        case _:
            return "<h1>Invalid input</h1>"

if __name__ == '__main__':
    app.run()
