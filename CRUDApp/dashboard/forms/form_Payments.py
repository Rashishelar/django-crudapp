from django.forms import ModelForm
from dashboard.models.payments import Payments
from django import forms

class Form_Payments(ModelForm):
    class Meta:
        model=Payments
        fields='__all__'
        widgets={
            'paymentID':forms.NumberInput(attrs={'class':'form-control'}),
            'customerNumber':forms.Select(attrs={'class':'form-control'}),
            'orderNumber':forms.Select(attrs={'class':'form-control'}),
            'paymentDate':forms.DateInput(attrs={'class':'form-control'}),
            'totalAmount':forms.NumberInput(attrs={'class':'form-control'}),
        }