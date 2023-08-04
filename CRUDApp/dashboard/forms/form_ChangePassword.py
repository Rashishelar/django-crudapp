from django import forms

class Form_ChangePassword(forms.Form):
    old_username=forms.CharField(max_length=20,label='User name',widget=forms.TextInput(attrs={'class':'form-control'}))
    old_password=forms.CharField(max_length=256,label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password=forms.CharField(max_length=256,label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

  