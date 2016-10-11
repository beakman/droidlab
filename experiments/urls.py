from django.conf.urls import url
from rest_framework import routers
from experiments.views import ExperimentList

router = routers.DefaultRouter()
router.register(r'experiments', ExperimentList)

urlpatterns = router.urls
