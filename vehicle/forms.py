from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('car_id', 'car_name', 'car_variant', 'car_fuel', 'car_color')
