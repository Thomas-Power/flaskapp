import mysql.connector

#Implementation of required functions for data retrieval and verification using MySQL server
class FlaskDatabase:
	#replace variables with appropriate credentials
	def __init__(self):
		self.db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="password",
			database="stock_data"
		)
		self.cursor = self.db.cursor()
	
	#retrieves graph info from database
	def select(self, values):
		sql = "SELECT * FROM graph_table WHERE ticker_name = %s"
		self.cursor.execute(sql, values)
		result = self.cursor.fetchall()
		return result
		
	def update(self, values):
		sql = "UPDATE graph_table SET ticker_name = %s, variables = %s WHERE id_number = %s"
		self.cursor.execute(sql, values)
		self.db.commit()
		
	#inserts time series values into database
	def insert(self, values):
		sql = "INSERT INTO graph_table (ticker_name, variables, id_number) VALUES (%s, %s, %s)"
		self.cursor.execute(sql, values)
		self.db.commit()
		
	#inserts time series values into database
	def delete(self, values):
		sql = "DELETE FROM graph_table WHERE id_number = %s"
		self.cursor.execute(sql, values)
		self.db.commit()