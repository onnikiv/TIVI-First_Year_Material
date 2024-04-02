# Mod 13 - Python-palvelinesimerkki Flaskilla

from flask import Flask, request, Response
import json

app = Flask(__name__)

def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

@app.route('/calc/<type>')
def calculate(type):
    # print(request.args.get('num1'))
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))

        if type == 'sum':
            result = sum(num1, num2) # http://localhost:3000/calc/sum?num1=3&num2=5

        elif type == 'multiply':
            result = multiply(num1, num2) # http://localhost:3000/calc/multiply?num1=3&num2=5

        else:
            response_body = json.dumps(
                {'error': 'Unknown calculation type.', 'status': 400}
            )
            return Response(response=response_body, status=400, mimetype='application/json')
        # oletuksena dictionary muutetaan http-vastaukseen automaattisesti jsoniksi
        # statuksella 200 (OK)
        return {'result': result, "numbers": [num1, num2]}
    
    except:
        # TODO: muuta virhekoodi myös http-vastauksen otsikkotiedoissa
        return {'error': 'Invalid parameters.', 'status': 400}


@app.errorhandler(404)
def page_not_found(error):
    # print(error)
    response_body = json.dumps(
                {'error': error.name,'description': error.description, 'status': error.code}
            )
    return Response(
        response=response_body,
        status=404,
        mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1',port=3000)

