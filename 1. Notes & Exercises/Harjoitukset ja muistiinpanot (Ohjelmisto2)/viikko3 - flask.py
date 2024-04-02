# Mod 13 - Python-palvelinesimerkki Flaskilla

from flask import Flask, request

app = Flask(__name__)

def calc_sum(a, b):
    return a + b

@app.route('/calc/sum')
def calculate():
    # print(request.args.get('num1'))
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return str(calc_sum(num1, num2))
    
    except:
        return 'Invalid parameters.'



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1',port=3000)

