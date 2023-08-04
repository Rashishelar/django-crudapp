from django.forms import ModelForm
from dashboard.models.orderdetails import Orderdetails
from django import forms

class Form_Orderdetails(ModelForm):
    class Meta:
        model=Orderdetails
        fields='__all__'
        widgets={
            'orderNumber':forms.Select(attrs={'class':'form-control'}),
            'productCode':forms.Select(attrs={'class':'form-control'}),
            'quantityOrdered':forms.NumberInput(attrs={'class':'form-control'}),
            'priceEach':forms.NumberInput(attrs={'class':'form-control'}),
            'orderLineNumber':forms.NumberInput(attrs={'class':'form-control'}),
        }