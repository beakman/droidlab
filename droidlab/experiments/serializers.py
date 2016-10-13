from rest_framework import serializers
from .models import Experiment, Result

class ResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = Result

class ExperimentSerializer(serializers.ModelSerializer):
	results = ResultSerializer(many=True, read_only=True)

	class Meta:
		model = Experiment


