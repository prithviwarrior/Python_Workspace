from pymysql import *

connection = Connection(
						host = "192.168.91.156",
						port = 3306,
						user = "anonymous",
						password = "12345678",
						db = "genesis",
						cursorclass = cursors.DictCursor
						);

cursor = connection.cursor()

#print(type(cursor)) #pymysql.cursor.Cursor
#query = "select * from student where id=1";
query = "select * from student where id=%s";
#query = "select * from student ";

cursor.execute(query,(1,));
1th
records = cursor.fetchall();

for record in records:
	print (record);
	#print(id[1])
	
connection.close()