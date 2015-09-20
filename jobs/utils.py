from gcm import GCM

GLOBAL_GCM_API_KEY = 'AIzaSyAGa2mz-Qw4izMSe9NRJ2dl4OKqHyQUY7c'
GLOBAL_REG_ID = ['APA91bH_s8KxnQmUuDOjKkE1mNcV2f2Fx9bcZScvhHg06BjHAlDYRqN5hvwfdo0lFTNdlcE2U4XGhwzd1MKjxopiI8_DOlnSztWGXFaL3sNtNxa7pkHOTxYYsHmDKz07wrh6ZI8iPv5o' ]
GLOBAL_DATA = { 'the_message':'test' , 'param2' :'value2' }


def trigger_gcm_request( API_KEY=None , REG_ID=None , data=None ) :

	global GLOBAL_GCM_API_KEY # importing the global variable into this method

	# mainly for test 
	global GLOBAL_REG_ID , GLOBAL_DATA
	


	# if no API key is passed, then we shall use the global one.
	if not API_KEY :
		API_KEY = GLOBAL_GCM_API_KEY

	if not data :
		data = GLOBAL_DATA

	if not REG_ID :
		REG_ID = GLOBAL_REG_ID		
	# doing the actual work of creating the request
	gcm = GCM( API_KEY )

	
	print "API KEY : %s , DATA : %s , REG_ID %s "%( API_KEY , data , REG_ID )

	response = gcm.json_request( REG_ID    , data=data)

	return response


def run_sql( sql_command ):
	import MySQLdb
	print "Executing SQLi %s"%( sql_command )

	db_creds = get_database_credentials()
	 
	db = MySQLdb.connect(host= db_creds['HOST'], # your host, usually localhost
                     user=db_creds['USER'], # your username
                      passwd=db_creds['PASSWORD'], # your password
                      db=db_creds['NAME']) # name of the data base

	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor() 

	# Use all the SQL you like
	cur.execute( sql_command )
	for row in cur.fetchall():
		print row[0]
	db.commit()	

def get_database_credentials():
	from http_task_gateway.settings import DATABASES
	db = DATABASES['default'] 

	return db
