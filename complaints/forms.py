from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta: 
        model = Complaint
        fields = ['title', 'description', 'photo', 'location', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }