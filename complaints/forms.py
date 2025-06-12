from django import forms
from .models import Complaint

class ComplaintForm(froms.ModelFrom):
    class Meta: 
        model = Complaint
        fields = ['tile', 'description', 'photo', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'lacation': froms.TextInput(attrs={'placeholder': 'e.g., Main Street, Block A'})
        }