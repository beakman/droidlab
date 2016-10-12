from django.contrib import admin

from .models import Experiment, Result

admin.site.register(Experiment)
admin.site.register(Result)