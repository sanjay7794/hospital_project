from django import template
from app.models import *

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    else:
        return 'bg-danger'


@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


@register.simple_tag
def is_state_selected(selected_state,pk):
    if selected_state==str(pk):
        return "selected"
    else:
        return ""    

@register.simple_tag
def is_city_selected(selected_city,pk):
    if selected_city==str(pk):
        return "selected"
    else:
        return ""         