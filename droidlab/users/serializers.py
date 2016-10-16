from rest_framework import serializers

from .models import User

from droidlab.experiments.models import Experiment
from droidlab.experiments.serializers import ExperimentSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
