from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Experiment, Result

class ResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = Result
		exclude = ('experiment',)

# class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
# 	results = serializers.HyperlinkedIdentityField(view_name="results-list")
	
# 	class Meta:
# 		model = Experiment
# 		fields = ('name', 'date', 'results')

class ExperimentSerializer(serializers.ModelSerializer):
	results = ResultSerializer(many=True)
	
	class Meta:
		model = Experiment
		fields = ('id', 'name', 'date', 'results')

	def create(self, validated_data):
		results_data = validated_data.pop('results')
		ex = Experiment.objects.create(**validated_data)
		for result_data in results_data:
			Result.objects.create(experiment=ex, **result_data)
		return ex

	def update(self, instance, validated_data):
		results_data = validated_data.pop('results')
		# Unless the application properly enforces that this field is
		# always set, the follow could raise a `DoesNotExist`, which
		# would need to be handled.
		results = instance.results

		instance.save()

		results.save()

		return instance

# class ResultHyperlink(serializers.HyperlinkedRelatedField):
#     # We define these as class attributes, so we don't need to pass them as arguments.
#     view_name = 'result-detail'
#     queryset = Result.objects.all()

#     def get_url(self, obj, view_name, request, format):
#         url_kwargs = {
#             'experiment_name': obj.experiment.name,
#             'experiment_pk': obj.pk
#         }
#         return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

#     def get_object(self, view_name, view_args, view_kwargs):
#         lookup_kwargs = {
#            'experiment__name': view_kwargs['experiment_name'],
#            'pk': view_kwargs['experiment_pk']
#         }
#         return self.get_queryset().get(**lookup_kwargs)