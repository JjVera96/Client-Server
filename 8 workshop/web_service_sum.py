from flask import Flask
from flask import request
import json


app = Flask(__name__)

@app.route('/sum/<int:operatorone>/<int:operatortwo>', methods=['GET'])
def sum(operatorone, operatortwo):

	value = operatorone + operatortwo
	response = {
		'answer' : value
	}

	return json.dumps(response)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)

