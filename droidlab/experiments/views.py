from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from .models import Experiment, Result
from .serializers import ExperimentSerializer, ResultSerializer

class ExperimentList(viewsets.ModelViewSet):
	queryset = Experiment.objects.all()
	serializer_class = ExperimentSerializer

class ResultList(viewsets.ModelViewSet):
	queryset = Result.objects.all()
	serializer_class = ResultSerializer
