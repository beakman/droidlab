from django.conf.urls import url
from rest_framework import routers
from droidlab.experiments.views import ExperimentList, ResultList

router = routers.DefaultRouter()
router.register(r'experiments', ExperimentList)
router.register(r'results', ResultList)

urlpatterns = router.urls
