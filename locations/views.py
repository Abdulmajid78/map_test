from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'add_location.html', {'form': form})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_list.html', {'locations': locations})