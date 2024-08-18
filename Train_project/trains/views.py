from django.shortcuts import render
from django.http import JsonResponse
from .models import Train
from .my_find_route_func import find_route_func
import json

def find_route_view(request):
    return render(request, 'trains/find_route.html')

def find_route(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_station = data.get('start')
        destination_station = data.get('destination')
        day = data.get('day')
        
        # For route of Train
        trains = find_route_func(start_station, destination_station, day)

        return JsonResponse({'trains': trains})
    return JsonResponse({'error': 'Invalid request'}, status=400)
