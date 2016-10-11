from rest_framework import serializers
from .models import Experiment, Result

class ExperimentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Experiment

class ResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = Result

