import json
import pandas as pd
from FlaskDatabase import FlaskDatabase

#Adapter class, used to verify and prepare data for input and output from database 
#and keep actual database implementation independent from greater system
class FlaskDatabaseAdapter:
	def __init__(self):
		self.db = FlaskDatabase()

	#inserts time series values into database
	def insert_graph(self, data):
		ticker_name = data["symbol"]
		variables = json.dumps(data)
		id_number = data["id_number"]
		self.db.insert([ticker_name, variables, id_number])
		
	def select(self, ticker_name):
		data = self.db.select([ticker_name])
		graphs = pd.DataFrame(data, columns=["ticker_name", "variables", "id_number"])
		return graphs