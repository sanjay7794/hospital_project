from django.shortcuts import render
from .models import *
def home(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    facilities=Facility.objects.all().order_by('pk')
    if selected_state_id:
        cities=City.objects.filter(state=selected_state_id)
    else:
        cities=City.objects.all()
    states=State.objects.all()
    hospitals=Hospital.objects.all()
    if selected_city_id:
        hospitals=hospitals.filter(city=City(selected_city_id))


    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'hospitals':hospitals,
        'selected_state':selected_state_id,
        'selected_city':selected_city_id


    }
    return render(request,'app/index.html',context)