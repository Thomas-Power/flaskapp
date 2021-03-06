import sys
sys.path.append('./fintech-lab')
from fintechlab.GraphFactory import GraphFactory
import pandas as pd
import time
import json
import os
from flaskDatabaseInit import flaskDatabaseInit
from FlaskDatabaseAdapter import FlaskDatabaseAdapter


class GraphRequestProcessor:
	def __init__(self):
		self.db = FlaskDatabaseAdapter()
		self.graph = GraphFactory()
		self.options = {
			"time series histogram":self.time_series_histogram,
			"time series adjusted gaussian":self.time_series_adjusted_gaussian,
			"time series gaussian":self.time_series_gaussian,
			"colormesh beta relationship":self.colormesh_beta_relationship,
			"beta relationship distribution slice":self.beta_relationship_distribution_slice,
			"traditional beta relationship":self.traditional_beta_relationship,
			"simple time series":self.simple_time_series,
			"series of gaussian probability of divergence from linear regression":self.series_of_gaussian_probability_of_divergence_from_linear_regression,
			"mean_return_over_x_days":self.mean_return_over_x_days
		}
		properties_file = open('app_properties.json')
		json_str = properties_file.read()
		properties = json.loads(json_str)
		self.req_list = properties["default_actions"]
		self.graph_dir = properties["graph_dir"]
		if not os.path.exists(self.graph_dir):
			os.makedirs(self.graph_dir) 
		
	def mean_return_over_x_days(self, data):
		symbol_one = data.get("symbol_one")
		relate_symbol = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		days_scope = int(data.get("days_scope")) if data.get("days_scope") != None else 10
		linear_regress = data.get("linear_regress")
		short = data.get("short")
		leveredge = float(data.get("leveredge")) if data.get("leveredge") != None else 1
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_all_mean_returns_over_x_days(symbol_one, start_date, end_date, relate_symbol, linear_regress, days_scope, short, leveredge, file_name=file_name)
	
	def time_series_histogram(self, data):
		symbol = data.get("symbol")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		bins = int(data.get("bins")) if data.get("bins") != None else 100
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_time_series_histogram(symbol, start_date, end_date, bins=bins, file_name=file_name)
		
	def time_series_gaussian(self, data):
		symbol_one = data.get("symbol_one")
		relate_value = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_time_series_gaussian(symbol, start_date, end_date, relate_value, file_name=file_name)
		
	def time_series_adjusted_gaussian(self, data):
		symbol_one = data.get("symbol_one")
		relate_value = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_time_series_adjusted_gaussian(symbol_one, start_date, end_date, relate_value, file_name=file_name)
		
	def colormesh_beta_relationship(self, data):
		symbol_one = data.get("symbol_one")
		symbol_two = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		days_scope = int(data.get("days_scope")) if data.get("days_scope") != None else 5
		bins = int(data.get("bins")) if data.get("bins") != None else 64
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_colormesh_beta_relationship(symbol_one, symbol_two, start_date, end_date, days_scope, bins, file_name=file_name)
			
		
	def beta_relationship_distribution_slice(self, data):
		symbol_one = data.get("symbol_one")
		symbol_two = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		percent_change = data.get("percent_change")
		days_scope = int(data.get("days_scope")) if data.get("days_scope") != None else 5
		bins = int(data.get("bins")) if data.get("bins") != None else 64
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_beta_relationship_distribution_slice(symbol_one, symbol_two, percent_change, start_date, end_date, days_scope, bins, file_name=file_name)
		
	def traditional_beta_relationship(self, data):
		symbol_one = data.get("symbol_one")
		symbol_two = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		days_scope = int(data.get("days_scope")) if data.get("days_scope") != None else 5
		linear_regress = data.get("linear_regress")
		file_name = self.graph_dir + data.get("id_number") + ".png"
		self.graph.source_beta_relationship(symbol_one, symbol_two, start_date, end_date, days_scope, file_name=file_name)
		
	def simple_time_series(self, data):
		symbol = data.get("symbol")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		linear_regress = data.get("linear_regress")
		file_name = self.graph_dir + data.get("id_number") + ".png"
		if linear_regress is None:
			self.graph.source_simple_time_series(symbol, start_date, end_date, file_name=file_name)
		else:
			self.graph.source_linear_regress_simple_time_series(symbol, start_date, end_date, file_name=file_name)
		
	def series_of_gaussian_probability_of_divergence_from_linear_regression(self, data):
		symbol_one = data.get("symbol_one")
		symbol_two = data.get("symbol_two")
		start_date = data.get("start_date")
		end_date = data.get("end_date")
		days_scope = int(data.get("days_scope")) if data.get("days_scope") != None else 5
		linear_regress = data.get("linear_regress")
		file_name = self.graph_dir + data.get("id_number") + ".png"
		if symbol_two is not None:
			self.graph.source_relational_series_of_gaussian_probability_of_divergence_from_linear_regression(symbol_one, symbol_two, start_date, end_date, days_scope, file_name=file_name)
		else:
			self.graph.source_series_of_gaussian_probability_of_divergence_from_linear_regression(symbol_one, start_date, end_date, days_scope, file_name=file_name)
	
	def get_ids(self, ticker_name):
		graphs = self.db.select(ticker_name)
		if len(graphs) == 0:
			graphs = self.create_default_set(ticker_name)
		else:
			self.create_if_not_available(graphs)
		id_numbers = str(list(graphs["id_number"]))
		for i in ['[',']','\'',' ']:
			id_numbers = id_numbers.replace(i, '')
		return id_numbers
		
	def create_default_set(self, ticker_name):
		for req in self.req_list:
			req["ticker_name"] = ticker_name
			req["symbol"] = ticker_name
			req["symbol_one"] = ticker_name
			req["id_number"] = str(time.time()).replace('.', '')
			self.db.insert_graph(req)
			self.create_graph(req)
		graphs = self.db.select(ticker_name)
		return graphs
	
	def create_if_not_available(self, graphs):
		for graph in graphs.itertuples():
			try:
				if not os.path.isfile(self.graph_dir + str(graph[3]) + ".png"):
					req = json.loads(str(graph[2]))
					self.create_graph(req)
			except IndexError:
				pass
	
	def update_graph(self, req):
		self.db.update_graph(req)
	
	def delete_graph(self, id_number):
		self.db.delete_graph(id_number)
	
	def save_graph_request(self, req):
		req["id_number"] = str(time.time()).replace('.', '')
		self.db.insert_graph(req)
		return req
		
	def create_graph(self, req):
		self.options[req["action"]](req)
		return req["id_number"]