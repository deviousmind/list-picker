from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/list', methods=['GET'])
def thing_list():
    things = ['thing1', 'thing2']
    return jsonify(things)


if __name__ == '__main__':
    app.run()
