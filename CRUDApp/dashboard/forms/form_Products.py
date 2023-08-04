from django.forms import ModelForm
from dashboard.models.products import Products
from django import forms

class Form_Products(ModelForm):
    class Meta:
        model=Products
        fields=['productCode','productName','productLine','productScale','productVendor','productDescription','quantityInStock','buyPrice','MSRP']
        widgets={
            'productCode':forms.TextInput(attrs={'class':'form-control'}),
            'productName':forms.TextInput(attrs={'class':'form-control'}),
            'productLine':forms.Select(attrs={'class':'form-control'}),
            'productScale':forms.TextInput(attrs={'class':'form-control'}),
            'productVendor':forms.TextInput(attrs={'class':'form-control'}),
            'productDescription':forms.Textarea(attrs={'class':'form-control'}),
            'quantityInStock':forms.NumberInput(attrs={'class':'form-control'}),
            'buyPrice':forms.NumberInput(attrs={'class':'form-control'}),
            'MSRP':forms.NumberInput(attrs={'class':'form-control'}),
            
        }