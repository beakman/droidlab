from __future__ import unicode_literals

from django.db import models

class Experiment(models.Model):
	# we take this data from the oml db name
	date = models.DateTimeField()

class Result(models.Model):
	# wich experiment belongs to
	experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)

	# oml database fields
	oml_tuple_id = models.IntegerField(null=True, blank=True)
	oml_sender_id = models.IntegerField(null=True, blank=True)
	oml_seq = models.IntegerField(null=True, blank=True)
	oml_ts_client = models.FloatField(null=True, blank=True)
	oml_ts_server = models.FloatField(null=True, blank=True)

	# -- testeldroid_gps
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	speed = models.FloatField(null=True, blank=True)
	
	# -- testeldroid_network
	networkType = models.IntegerField(null=True, blank=True)
	cellId
	lacId = models.IntegerField(null=True, blank=True)
	rssi = models.IntegerField(null=True, blank=True)
	networkId = models.IntegerField(null=True, blank=True)
	cellPsc = models.IntegerField(null=True, blank=True)
	rsrp = models.IntegerField(null=True, blank=True)
	snr = models.IntegerField(null=True, blank=True)
	cqi = models.IntegerField(null=True, blank=True)
	rsrq = models.IntegerField(null=True, blank=True)
	
	# -- testeldroid_neighbours
	psc = models.IntegerField(null=True, blank=True)
	rssi = models.IntegerField(null=True, blank=True)
	code = models.IntegerField(null=True, blank=True)
	
	# testeldroid_battery
	power_consumption = models.IntegerField(null=True, blank=True)

	# -- testeldroid_profile
	ip = models.CharField(max_length=250)
	scenario = models.CharField(max_length=250)
	tech = models.CharField(max_length=250)
	config = models.CharField(max_length=250)
	device = models.CharField(max_length=250)
	device_conf = models.CharField(max_length=250)
	imei = models.CharField(max_length=250)
	os_version = models.CharField(max_length=250)
	operator = models.CharField(max_length=250)
	capture_id = models.CharField(max_length=250)
	comments = models.CharField(max_length=250)