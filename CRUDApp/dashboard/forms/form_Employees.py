from django.forms import ModelForm
from dashboard.models.employees import Employees
from django import forms

class Form_Employees(ModelForm):
    class Meta:
        model=Employees
        fields='__all__'
        widgets={
            'employeeNumber':forms.NumberInput(attrs={'class':'form-control'}),
            'lastName':forms.TextInput(attrs={'class':'form-control'}),
            'firstName':forms.TextInput(attrs={'class':'form-control'}),
            'extension':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'officeCode':forms.Select(attrs={'class':'form-control'}),
            'reportsTo':forms.Select(attrs={'class':'form-control'}),
            'jobTitle':forms.TextInput(attrs={'class':'form-control'}),
        }