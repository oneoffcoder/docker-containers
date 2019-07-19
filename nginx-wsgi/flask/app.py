import json
import os

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
CORS(app, resources={r'/*': {
    'origins': '*',
    'supports_credentials': True,
    'allow_headers': '*'
}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Accept,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, HEAD, POST, OPTIONS, PUT, PATCH, DELETE')
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return json.dumps({'message': 'no one was here'})


@app.route('/v1/test', methods=['GET'])
def hello():
    h = {}
    for k, v in request.headers.items():
        h[k] = v

    return json.dumps(h)


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    print('final port is {}'.format(port))
    app.run(debug=False, host='0.0.0.0', port=port)
