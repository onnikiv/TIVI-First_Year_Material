from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route(f'/alkuluku/<int:luku>', methods=['GET'])
def alkuluku(luku):
    try:
        if luku < 2:
            return {'error': 'Number must be greater than 1.', 'status': 400}
        elif luku == 2:
            return {'Number': luku, 'isPrime': True}
        else:
            for i in range(2, luku):
                if luku % i == 0:
                    return {'isPrime': False, 'number': luku}
            return {'Number': luku, 'isPrime': True}
    except ValueError:
        return {'error': 'Invalid parameters.', 'status': 400}


@app.errorhandler(404)
def page_not_found(error):
    response_body = json.dumps(
        {'error': error.name, 'description': error.description, 'status': error.code}
    )
    return Response(
        response=response_body,
        status=404,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
