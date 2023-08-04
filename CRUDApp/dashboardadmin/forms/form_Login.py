from django.forms import ModelForm
from dashboard.models.admin import Admin
from django import forms

class Form_Login(ModelForm):
    class Meta:
        model=Admin
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }