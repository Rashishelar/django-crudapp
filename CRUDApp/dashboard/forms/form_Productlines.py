from django.forms import ModelForm
from dashboard.models.productlines import Productlines
from django import forms

class Form_Productlines(ModelForm):
    class Meta:
        model=Productlines
        fields='__all__'
        widgets={
            'productLine':forms.TextInput(attrs={'class':'form-control'}),
            'textDescription':forms.Textarea(attrs={'class':'form-control'}),
        }