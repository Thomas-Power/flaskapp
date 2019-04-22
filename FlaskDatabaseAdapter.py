import json
import pandas as pd
from FlaskDatabase import FlaskDatabase

#Adapter class, used to verify and prepare data for input and output from database 
#and keep actual database implementation independent from greater system
class FlaskDatabaseAdapter:
	def __init__(self):
		self.db = FlaskDatabase()

	def update_graph(self, data):
		variables = json.dumps(data)
		id_number = data["id_number"]
		self.db.update([variables, id_number])

	def insert_graph(self, data):
		ticker_name = data["ticker_name"]
		variables = json.dumps(data)
		id_number = data["id_number"]
		self.db.insert([ticker_name, variables, id_number])
		
	def select(self, ticker_name):
		data = self.db.select([ticker_name])
		graphs = pd.DataFrame(data, columns=["ticker_name", "variables", "id_number"])
		return graphs
		
	def delete_graph(self, id_number):
		self.db.delete([id_number])