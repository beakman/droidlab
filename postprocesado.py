#!/usr/bin/env python
import os
import sys
import string
from datetime import datetime
import random
import psycopg2
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
import django
django.setup()

from droidlab.experiments.models import Experiment, Result

# IMPROVE: No estaria mal asegurar esto
HOST='localhost'
PORT='5432'
USER='oml'
PASSWORD='tester'
DBNAME = sys.argv[1]

# genera experimentos aleatorios
s = string.lowercase+string.digits
start_date = datetime.today().replace(day=1, month=1).toordinal()
end_date = datetime.today().toordinal()
random_day = datetime.fromordinal(random.randint(start_date, end_date))

def generaResultados(experimento):
	res = Result(
			experiment=experimento,
			oml_tuple_id=random.randint(1,30), 
			oml_sender_id=random.randint(1,30), 
			oml_seq=random.randint(1,30), 
			oml_ts_client=random.random(),
			oml_ts_server=random.random(),
			timestamp=random_day.strftime('%d/%M/%Y%H:%m:%s,%S'),
			latitude=random.random(),
			longitude=random.random(),
			speed=random.random(),
			networkType=random.randint(1,30),
			cellId=random.randint(1,30),
			lacId=random.randint(1,30),
			rssi_network=random.randint(1,30),
			networkId=random.randint(1,30),
			cellPsc=random.randint(1,30),
			rsrp=random.randint(1,30),
			snr=random.randint(1,30),
			cqi=random.randint(1,30),
			rsrq=random.randint(1,30),
			psc=random.randint(1,30),
			rssi_neighbours=random.randint(1,30),
			code=random.randint(1,30),
			power_consumption=random.randint(1,30),
			ip=''.join(random.sample(s,10)),
			scenario=''.join(random.sample(s,10)),
			tech=''.join(random.sample(s,10)),
			config=''.join(random.sample(s,10)),
			device=''.join(random.sample(s,10)),
			device_conf=''.join(random.sample(s,10)),
			imei=''.join(random.sample(s,10)),
			os_version=''.join(random.sample(s,10)),
			operator=''.join(random.sample(s,10)),
			capture_id=''.join(random.sample(s,10)),
			comments=''.join(random.sample(s,10))
			)
	res.save()

# IMPROVE: COMPROBAR SI YA EXISTE DB CON ESE NOMBRE
exp = Experiment(date=datetime.today(), name=DBNAME)
exp.save()

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
	width = tmp[i][6]
	height = tmp[i][7]
	res = Result(
			experiment=exp,
			oml_tuple_id=oml_tuple_id, 
			oml_sender_id=oml_sender_id, 
			oml_seq=oml_seq, 
			oml_ts_client=oml_ts_client,
			oml_ts_server=oml_ts_server,
			timestamp=timestamp,
			width=width,
			height=height
			)
	res.save()
	# tengo que serializar esto para mandarlo