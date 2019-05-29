from flask import Flask, request, jsonify
from algorithm import approx
from worker import integrate

app = Flask(__name__)
TASKS = {}

@app.route('/', methods=["GET"])
def list_tasks():
	tasks = { task_id: {'ready':task.ready}
			  for task_id, task in TASKS.item()}
	return jsonify(tasks)

@app.route('/', methods = ['PUT'])
def put_task():
	f = request.json['f']
	a = request.json['a']
	b = request.json['b']
	c = request.json['c']
	d = request.json['d']
	size = request.json.get('size',100)

	response = {
		'result': integrate.delay(f,a,b,c,d,size),
	}
	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True) 