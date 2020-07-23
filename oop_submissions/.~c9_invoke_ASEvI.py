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


def table():
	query="""
		CREATE TABLE	Student
		(
			student_id INT,
			name VARCHAR(100),
			age INT
		);
	"""
	write_data(query)

def insert():
	a=[(1,'shaji',24),(2,'yaswanth',22),(3,'lingam',20)]
	
	for i in a:
		
		query="""
			INSERT INTO Student VALUES{}
		""".format(i)
		write_data(query)


def get_info():
	query="""
			SELECT name FROM Student WHERE age>=20 AND student_id>1;
	"""
	info =read_data(query)
	print(info)
	print()
	query="""
			SELECT name FROM Student WHERE age>=20 OR student_id>1;
	"""
	info =read_data(query)
	print(info)
	print()
	
	query="""
			SELECT name FROM Student WHERE age>20 AND (name='shaji' OR name='lingam');
	"""
	info =read_data(query)
	print(info)
	print()
	
	query="""
			SELECT name FROM Student WHERE NOT age>20 OR student_id>1;
	"""
	info =read_data(query)
	print(info)
	
	
	
	
	
	return info

