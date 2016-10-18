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

    def get_queryset(self):
        queryset = super(ExperimentList, self).get_queryset()
        return queryset.filter(user=self.request.user)

class ExperimentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Experiment
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    lookup_field = 'name'

class ResultList(generics.ListCreateAPIView):
    model = Result
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        queryset = super(ResultList, self).get_queryset()
        return queryset.filter(experiment__name=self.kwargs.get('name'))

    def perform_create(self, serializer):
    	experiment = Experiment.objects.get(name=self.kwargs.get('name'))
        serializer.save(experiment=experiment)

class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Result
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        queryset = super(ResultDetail, self).get_queryset()
        return queryset.filter(id=self.kwargs.get('pk'))
