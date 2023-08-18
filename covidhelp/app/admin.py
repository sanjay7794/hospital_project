from django.contrib import admin
from .models import *
# Register your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=Hospital)
def afterHospitalSave(signal,instance,**kwargs):
    service = Services(hospital=instance)
    service.save()

    
admin.site.register(State)
admin.site.register(City)
admin.site.register(Hospital)
admin.site.register(Services)
