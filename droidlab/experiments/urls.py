from django.conf.urls import url, include
from rest_framework import routers

from droidlab.experiments.views import ExperimentList, ExperimentDetail
from droidlab.experiments.views import ResultList, ResultDetail

# router = routers.DefaultRouter()
# router.register(r'experiments', ExperimentList, base_name='experiments')
# router.register(r'results', ResultList, base_name='result')

# urlpatterns = router.urls

urlpatterns = [
    url(r'^(?P<name>[-\w.]+)/results/(?P<pk>\d+)$', ResultDetail.as_view(), name='result-detail'),
    url(r'^(?P<name>[-\w.]+)/results$', ResultList.as_view(), name='result-list'),
    url(r'^(?P<name>[-\w.]+)$', ExperimentDetail.as_view(), name='experiment-detail'),
    url(r'^$', ExperimentList.as_view(), name='experiment-list')
]
