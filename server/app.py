from flask import Flask, json, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin
import algorithm
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
RESULT = [1,3,5]
output = {}
@app.route('/algorithm', methods=['GET', 'POST'])
@cross_origin()
def call_algorithm():
    if request.method == 'POST':
        post_data = request.get_json()
        result = algorithm.test(post_data)
        output['result'] = result
    return jsonify(output)
if __name__ == '__main__':
    app.run()
    
