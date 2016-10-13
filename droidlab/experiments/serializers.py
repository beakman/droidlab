from rest_framework import serializers
from .models import Experiment, Result

class ResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = Result

class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
	results = serializers.HyperlinkedIdentityField(view_name="results-list")
	
	class Meta:
		model = Experiment
		fields = ('name', 'date', 'results')


