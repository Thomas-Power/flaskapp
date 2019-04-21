import mysql.connector

#Initializes MySQL database and necessary tables
class flaskDatabaseInit:
	def setup(self):
		self.build_database_and_connect()
		self.build_table()

	def build_database_and_connect(self):
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="password"
		)
		mycursor = db.cursor()
		mycursor.execute("SHOW DATABASES")
		no_database = True

		for x in mycursor:
			if(x[0] == "stock_data"):
				no_database = False

		if no_database:
			mycursor.execute("SHOW DATABASES")
			mycursor.execute("CREATE DATABASE stock_data")


	def build_table(self):
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="password",
			database="stock_data"
		)
		mycursor = db.cursor()
		mycursor.execute("SHOW TABLES")
		no_table = True

		for x in mycursor:
			if x[0] == "graph_table":
				no_table = False

		if no_table:
			mycursor.execute("CREATE TABLE graph_table (ticker_name VARCHAR(255), variables VARCHAR(1200), id_number VARCHAR(255), UNIQUE(id_number))")
		