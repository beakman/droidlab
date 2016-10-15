from __future__ import unicode_literals

from django.db import models

class Experiment(models.Model):
	name = models.CharField(unique=True, max_length=255)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Result(models.Model):
	# wich experiment belongs to
	experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='results')

	# oml database common fields
	oml_tuple_id = models.IntegerField(null=True, blank=True)
	oml_sender_id = models.IntegerField(null=True, blank=True)
	oml_seq = models.IntegerField(null=True, blank=True)
	oml_ts_client = models.FloatField(null=True, blank=True)
	oml_ts_server = models.FloatField(null=True, blank=True)
	timestamp = models.CharField(max_length=100, blank=True)

	# -- testeldroid_gps
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	speed = models.FloatField(null=True, blank=True)
	
	# -- testeldroid_network
	networkType = models.IntegerField(null=True, blank=True)
	cellId = models.IntegerField(null=True, blank=True)
	lacId = models.IntegerField(null=True, blank=True)
	rssi_network = models.IntegerField(null=True, blank=True)
	networkId = models.IntegerField(null=True, blank=True)
	cellPsc = models.IntegerField(null=True, blank=True)
	rsrp = models.IntegerField(null=True, blank=True)
	snr = models.IntegerField(null=True, blank=True)
	cqi = models.IntegerField(null=True, blank=True)
	rsrq = models.IntegerField(null=True, blank=True)
	
	# -- testeldroid_neighbours
	psc = models.IntegerField(null=True, blank=True)
	rssi_neighbours = models.IntegerField(null=True, blank=True)
	code = models.IntegerField(null=True, blank=True)
	
	# testeldroid_battery
	power_consumption = models.IntegerField(null=True, blank=True)

	# -- testeldroid_profile
	ip = models.CharField(max_length=250, blank=True)
	scenario = models.CharField(max_length=250, blank=True)
	tech = models.CharField(max_length=250, blank=True)
	config = models.CharField(max_length=250, blank=True)
	device = models.CharField(max_length=250, blank=True)
	device_conf = models.CharField(max_length=250, blank=True)
	imei = models.CharField(max_length=250, blank=True)
	os_version = models.CharField(max_length=250, blank=True)
	operator = models.CharField(max_length=250, blank=True)
	capture_id = models.CharField(max_length=250, blank=True)
	comments = models.CharField(max_length=250, blank=True)

	# video
	width = models.IntegerField(null=True, blank=True)
	height = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return 'Result for ' + self.experiment.name