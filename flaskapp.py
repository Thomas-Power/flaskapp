from flask import Flask, request, jsonify
from flask_cors import CORS
from flaskDatabaseInit import flaskDatabaseInit
from GraphRequestProcessor import GraphRequestProcessor

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

graph_requests = GraphRequestProcessor()

@app.route('/create_graph', methods=['GET', 'POST'])
def create_graph():
	data = request.args
	if data["id_number"] == "new":
		return new_graph(data) 
	else:
		return update_graph(data)
	
def update_graph(data):
	data = request.args
	graph_requests.update_graph(data)
	id_number = graph_requests.create_graph(data)
	return id_number

def new_graph(data):
	data = request.args.to_dict()
	graph_req = graph_requests.save_graph_request(data)
	id_number = graph_requests.create_graph(graph_req)
	return id_number

	
@app.route('/graph_ids', methods=['GET', 'POST'])
def request_graph_ids():
	data = request.args
	ticker_name = data["ticker_name"]
	id_numbers = graph_requests.get_ids(ticker_name)
	return id_numbers
	
@app.route('/delete_graph', methods=['GET', 'POST'])
def delete_graph():
	data = request.args
	id_number = data["id_number"]
	graph_requests.delete_graph(id_number)
	return "successfully deleted"
	
if __name__ == '__main__':
	dbinit = flaskDatabaseInit()
	dbinit.setup()
	app.run(debug=True)