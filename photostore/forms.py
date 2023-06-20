from django import forms
from .models import Caption
from django.forms import ModelForm

class CaptionForm(ModelForm):
    class Meta:
        model = Caption
        fields = '__all__'

# declaring the ModelForm
class EditCaptionForm(ModelForm):
    
    class Meta:
        # the Model from which the form will inherit from
        model = Caption
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes
        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'continent': forms.TextInput(attrs={'class': 'form-control'}),
             'country': forms.TextInput(attrs={'class': 'form-control'}),
             'price': forms.TextInput(attrs={'class': 'form-control'}),
             'imageID': forms.TextInput(attrs={'class': 'form-control'}),
             'image': forms.TextInput(attrs={'class': 'form-control'}),
        }

