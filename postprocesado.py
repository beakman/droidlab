#!/usr/bin/env python
import os
import sys
import string
from datetime import datetime
import random
import psycopg2
import requests
import json

# IMPROVE: No estaria mal asegurar esto
HOST='localhost'
PORT='5432'
USER='oml'
PASSWORD='tester'
DBNAME = sys.argv[1]
API_URL = 'https://droidlab.herokuapp.com/api/'
AUTH_TOKEN = 'Token 7ebbd9dda9528bf296d1877223e0dcb116fca9b0'

# genera experimentos aleatorios
s = string.lowercase+string.digits
start_date = datetime.today().replace(day=1, month=1).toordinal()
end_date = datetime.today().toordinal()
random_day = datetime.fromordinal(random.randint(start_date, end_date))

# Primero creamos el experimento:

data = {}
data['name'] = DBNAME
data['results'] = []
json_data = json.dumps(data)

print '\n [*] json_data: '
print json_data

response = requests.post(API_URL, data=json_data, headers={'Authorization': AUTH_TOKEN, 'content-type': 'application/json'})

print '[*] POST to API_URL: ' + API_URL
print '[*] Response: ' + str(response.status_code)

# Abrimos la base de datos e iteramos por las filas
conn = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
cursor = conn.cursor()

# Video
#
# [(1, 1, 0, 0.451, 1476374538.07106, '13.10.201618.02.18.815', '640', '360')]
cursor.execute('SELECT * FROM video;')
tmp = cursor.fetchall()
for i in range(len(tmp)):
	oml_tuple_id = tmp[i][0] 
	oml_sender_id = tmp[i][1]
	oml_seq = tmp[i][2]
	oml_ts_client = tmp[i][3]
	oml_ts_server = tmp[i][4]
	timestamp = tmp[i][5]
	width = int(tmp[i][6])
	height = int(tmp[i][7])

	print '\nGet data from database: \n'
	print '[*]  oml_tuple_id= ' + str(oml_tuple_id)
	print '[*]  oml_sender_id= ' + str(oml_sender_id)
	print '[*]  oml_seq= ' + str(oml_seq)
	print '[*]  oml_ts_client= ' + str(oml_ts_client)
	print '[*]  oml_ts_server= ' + str(oml_ts_server)
	print '[*]  timestamp= ' + str(timestamp)
	print '[*]  width= ' + str(width)
	print '[*]  height= ' + str(height)

	url = API_URL + DBNAME + '/results'
	
	data = {}
	data['oml_tuple_id'] = oml_tuple_id
	data['oml_sender_id'] = oml_sender_id
	data['oml_seq'] = oml_seq
	data['oml_ts_client'] = oml_ts_client
	data['oml_ts_server'] = oml_ts_server
	data['timestamp'] = timestamp
	data['width'] = width
	data['height'] = height

	json_data = json.dumps(data)
	
	print '\n [*] json_data: '
	print json_data
	
	response = requests.post(url, data=json_data, headers={'Authorization': AUTH_TOKEN, 'content-type': 'application/json'})
	print '[*] POST to API endpoint: ' + url
	print '[*] Response: ' + str(response.status_code)
	# tengo que serializar esto para mandarlo