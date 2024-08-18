from django.contrib import admin
from .models import Train, Day
from .forms import TrainForm

class TrainAdmin(admin.ModelAdmin):
    form = TrainForm
    list_display = ('train_name', 'start', 'destination', 'starting_time', 'reaching_time', 'get_days')

admin.site.register(Train, TrainAdmin)
admin.site.register(Day)

from trains.models import Day

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in days:
    Day.objects.get_or_create(name=day)
