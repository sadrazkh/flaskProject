from flask import Flask, jsonify, request

app = Flask(__name__)


# POST -> Used to receive data
# GET -> Used to send data back only


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    return request_data['name']


@app.route('/store/<string:name>')
def get_store(name):
    return jsonify({'names': name})


if __name__ == '__main__':
    app.run()
