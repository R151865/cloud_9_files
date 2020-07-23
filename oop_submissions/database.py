def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

def data_1():
	query="""
		CREATE TABLE R
		(	id PRIMARY KEY,
			a_id VARCHAR(10),
			b_id INT
		);
	"""
	write_data(query)

def insert_data_1():
	query="""
		INSERT INTO R(id,a_id,b_id) 
		VALUES
		(1,'a1',101),
		(2,'a2',102),
		(3,'a2',103)
		"""
	write_data(query)
	
def data_2():
	query="""
		CREATE TABLE S
		(	id PRIMARY KEY,
			a_id VARCHAR(10),
			b_id INT
		);
	"""
	write_data(query)

def insert_data_2():
	query="""
		INSERT INTO S(id,a_id,b_id) 
		VALUES
		(1,'a2',103),
		(2,'a3',104)
		"""
	write_data(query)
	


	
def get_info():
	print('yes')
	query="""(SELECT * FROM R) UNION ALL (SELECT * FROM S);
		"""
	info=read_data(query)
	print('yes')
	for i in info:
		print(i)
	print()
	return info

