from django.forms import ModelForm
from dashboard.models.orders import Orders
from django import forms

class Form_Orders(ModelForm):
    class Meta:
        model=Orders
        fields='__all__'
        
        widgets={
            'orderNumber':forms.NumberInput(attrs={'class':'form-control'}),
            'orderDate':forms.DateInput(attrs={'class':'form-control'}),
            'requiredDate':forms.DateInput(attrs={'class':'form-control'}),
            'shippedDate':forms.DateInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
            'comments':forms.Textarea(attrs={'class':'form-control'}),
            'customerNumber':forms.Select(attrs={'class':'form-control'}),
        }
        