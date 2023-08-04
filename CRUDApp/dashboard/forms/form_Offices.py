from django.forms import ModelForm
from dashboard.models.offices import Offices
from django import forms

class Form_Offices(ModelForm):
    class Meta:
        model=Offices
        fields='__all__'
        widgets={
            'officeCode':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'addressLine1':forms.TextInput(attrs={'class':'form-control'}),
            'addressLine2':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'postalCode':forms.TextInput(attrs={'class':'form-control'}),
            'territory':forms.TextInput(attrs={'class':'form-control'}),
        }