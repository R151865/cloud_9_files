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
	


Q1="""
        CREATE TABLE User
        (
            user_id INT PRIMARY KEY,
            first_name VARCHAR(200) NOT NULL,
            last_name VARCHAR(200) NOT NULL,
            address VARCHAR(300) NOT NULL,
            phone_number INT NOT NULL
        
        );
    """



Q2="""
        CREATE TABLE Post_User1
        (
            user_id INT ,
            post_id INT AUTOINCREMENT PRIMARY KEY,
            post_content VARCHAR(500),
            CONSTRAINT 
            FOREIGN KEY(user_id) REFERENCES User(user_id)
            ON DELETE CASCADE
        );
        """

Q3="""
    INSERT INTO User(user_id,first_name,last_name,address,phone_number)
    VALUES
    (1,'tony','stark','new york',1234567890)
 """

Q4="""
    INSERT INTO User(user_id,first_name,last_name,address,phone_number)
    VALUES
    (2,'john','wick','la',987654321)
"""
    
    

Q5="""
    INSERT  INTO Post_User(user_id,post_content)
    VALUES(2,'my first post');
"""

Q6="""
    SELECT * FROM User;
"""
Q7="""
        SELECT first_name,last_name FROM User;
"""

Q8="""
    UPDATE User SET first_name='thor',last_name='ragnarok' WHERE first_name='tony' AND last_name='stark';
"""


Q9="""
    INSERT  INTO Post_User(user_id,post_id,post_content) VALUES(1,1,'My Second Post');
"""
Q10="""
    DELETE FROM User WHERE first_name='john' AND last_name='wick';
"""

Q11="""
    DELETE FROM Post_User;
"""

#Create a post for tony stark with post_content as my first post