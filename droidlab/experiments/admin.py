from django.contrib import admin

from .models import Experiment, Result

class ExperimentAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'date', 'user')
    
    def save_model(self, request, obj, form, change):
        if not obj.user.id:
            obj.user = request.user
        obj.save()

admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Result)