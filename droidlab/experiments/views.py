# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework import viewsets

# from .models import Experiment, Result
# from .serializers import ExperimentSerializer, ResultSerializer

# class ExperimentList(viewsets.ModelViewSet):
# 	queryset = Experiment.objects.all()
# 	serializer_class = ExperimentSerializer

# class ResultList(viewsets.ModelViewSet):
# 	queryset = Result.objects.all()
# 	serializer_class = ResultSerializer

from rest_framework import generics, permissions

from .models import Experiment, Result
from .serializers import ExperimentSerializer, ResultSerializer

class ExperimentList(generics.ListCreateAPIView):
    model = Experiment
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

class ExperimentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Experiment
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    lookup_field = 'name'

class ResultList(generics.ListCreateAPIView):
    model = Result
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Result
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        queryset = super(ResultDetail, self).get_queryset()
        return queryset.filter(id=self.kwargs.get('pk'))
