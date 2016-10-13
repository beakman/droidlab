from django.conf.urls import url
from rest_framework import routers
from droidlab.experiments.views import ExperimentList, ResultList

router = routers.DefaultRouter()
router.register(r'experiments', ExperimentList, base_name='experiments')

urlpatterns = router.urls
