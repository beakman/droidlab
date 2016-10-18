from django.conf.urls import url, include

from droidlab.experiments.views import ResultDetail, ResultList, ExperimentDetail, ExperimentList
from droidlab.users.views import ListUsers, UserDetail, RetrieveCurrentUser

# Experiments api endpoints
urlpatterns = [
    url(r'^experiments/(?P<name>[-\w.]+)/results/(?P<pk>\d+)$', ResultDetail.as_view(), name='result-detail'),
    url(r'^experiments/(?P<name>[-\w.]+)/results$', ResultList.as_view(), name='result-list'),
    url(r'^experiments/(?P<name>[-\w.]+)$', ExperimentDetail.as_view(), name='experiment-detail'),
    url(r'^experiments$', ExperimentList.as_view(), name='experiment-list')
]

# Users api endpoints
urlpatterns = [
    url(r'^users$', ListUsers.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^me', RetrieveCurrentUser.as_view()),
]