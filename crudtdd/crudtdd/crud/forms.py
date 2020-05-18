from django import forms
from .models import list_Model
class list_Form(forms.ModelForm):
    class Meta:
         model = list_Model
         fields = [
             'name'
        ]