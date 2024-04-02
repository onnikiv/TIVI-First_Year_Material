# Mod 13 - Python-palvelinesimerkki Flaskilla

from flask import Flask, request, Response

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
            
            response_body = {'error': 'Unknown calculation type.', 'status': 400}
            return Response(response=response_body, status=400)
        return {'result': result, "numbers": [num1, num2]}
    
    except:
        return {'error': 'Invalid parameters.', 'status': 400}



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1',port=3000)

