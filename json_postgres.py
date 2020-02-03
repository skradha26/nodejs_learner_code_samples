import json
import psycopg2
from psycopg2.extras import Json 
#import urllib.parse as urlp

row = {}
def copyjsontopostgres():
	try:
		print("connecting to postgres database")
		#just a sample database and table with public data
		conn = psycopg2.connect(host="localhost",database="food",user="user1",password="pass")
		cur = conn.cursor()
		cur.execute('SELECT VERSION()')
		print("CONNECTION OPEN")
		db_version = cur.fetchone()
		print(db_version)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	#return conn

	with open('data.json') as data_file:
	    data = json.load(data_file)
	    #print(len(data))
	    for v in data.values():
	    	print(len(v))
	    	for i in range(0,len(v)):
	    		#print(v[i])
	    		y = v[i]
	    		jsonformat = json.dumps(y)
	    		print(jsonformat)
	    		jsonformat = "'{}'".format(jsonformat)
	    		print("after formatting",jsonformat)
	    		print(i)
	    		query = "INSERT INTO foodrecalls(info) VALUES({})".format(jsonformat)
	    		print(i)
	    		cur.execute(query)
	    		
	    		conn.commit()
	    	
	    	


	#print(json_data[0])



	try:
		conn.close()
		print('closed connection')
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

if __name__ == "__main__":
	copyjsontopostgres()




		
# with open('data.json') as data_file:
#     data = json.load(data_file)
#     for v in data:
#         item = {}
#         item[v] = data[v]
#         json_data = json.dumps(data)
#     print(json_data)
