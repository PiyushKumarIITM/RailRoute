from django import forms
from .models import Train

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
        widgets = {
            'starting_time': forms.TimeInput(attrs={'type': 'time'}),
            'reaching_time': forms.TimeInput(attrs={'type': 'time'}),
        }
