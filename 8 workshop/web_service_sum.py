from flask import Flask
from flask import request
from flask_json import FlaskJSON, json_response

app = Flask(__name__)
json = FlaskJSON(app)
json.init_app(app)

@app.route('/sum/<int:operatorone>/<int:operatortwo>', methods=['GET'])
def sum(operatorone, operatortwo):

	value = operatorone + operatortwo
	return json_response(data=value, headers_={'X-STATUS': 'ok'})

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

