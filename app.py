from flask import Flask,render_template,jsonify
from flask import request
import json
import os
import mysql.connector
app = Flask(__name__)


@app.route('/contest')
def holidify():
	#return "The placeCode is " + placeCode


	#testjsoon()
	#return json.dumps(json_data)
	return render_template('/index.html')




if __name__ == '__main__':
	app.run(debug=True)
