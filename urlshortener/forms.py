from django import forms
from .models import ModelData

class ModelDataForm(forms.ModelForm):
    widget = forms.URLInput(attrs={'class': 'form-control form-control lg', 'placeholder': 'Enter your URL here ...'})
    url = forms.URLField(widget=widget)

    class Meta:
        model = ModelData
        fields = {'url',}

