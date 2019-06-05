from django import forms
from .models import Employee_detail

class Employee_detailForm(forms.ModelForm):
    
    class Meta:
        model = Employee_detail
        fields = ('name','id','salary','department','gender')
