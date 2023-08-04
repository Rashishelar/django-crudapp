from django.forms import ModelForm
from dashboard.models.customers import Customers
from django import forms

class Form_Customers(ModelForm):
    class Meta:
        model=Customers
        fields='__all__'
        widgets={
            'customerNumber':forms.NumberInput(attrs={'class':'form-control'}),
            'customerName':forms.TextInput(attrs={'class':'form-control'}),
            'contactLastName':forms.TextInput(attrs={'class':'form-control'}),
            'contactFirstName':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'addressLine1':forms.TextInput(attrs={'class':'form-control'}),
            'addressLine2':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'postalCode':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'salesRepEmployeeNumber':forms.Select(attrs={'class':'form-control'}),
            'creditLimit':forms.NumberInput(attrs={'class':'form-control'})
        }