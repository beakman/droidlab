#!/usr/bin/env python
from datetime import datetime
import random
import string
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
import django
django.setup()

from droidlab.experiments.models import Experiment, Result

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
			timestamp=random_day.strftime('%d.%m.%Y%H.%M.%S.%f')[:-3], # "dd.MM.yyyyHH.mm.ss.SSS"
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

exp = Experiment(date=datetime.today(), name='nc_'+ random_day.strftime('%d.%M.%Y%H.%m.%S.%f')[:-3])
exp.save()

for x in xrange(1,10):
	print "Generando resultado " + str(x)
	generaResultados(exp)