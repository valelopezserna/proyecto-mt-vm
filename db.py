# -*- coding: utf-8 -*-

import pymysql

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'proyecto'

def Run_query(query=''):
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

	conn = pymysql.connect(*datos)
	cursor = conn.cursor()
	cursor.execute(query)

	if query.upper().startswith('SELECT'):
		data = cursor.fetchall()
	else:
		conn.commit()
		data = None

	cursor.close()
	conn.close()
	return data






