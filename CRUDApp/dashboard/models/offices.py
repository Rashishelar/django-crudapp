from django.db import models

class Offices(models.Model):
    officeCode=models.CharField(max_length=10,verbose_name='Office Code',null=False,primary_key=True)
    city=models.CharField(max_length=50,verbose_name='City',null=False)
    phone=models.CharField(max_length=50,verbose_name='Phone',null=False)
    addressLine1=models.CharField(max_length=50,verbose_name='Address Line 1',null=False)
    addressLine2=models.CharField(max_length=50,verbose_name='Address Line 2',default='',null=True)
    state=models.CharField(max_length=50,verbose_name='State',default='',null=True)
    country=models.CharField(max_length=50,verbose_name='Country',null=False)
    postalCode=models.CharField(max_length=15,verbose_name='Postal Code',null=False)
    territory=models.CharField(max_length=10,verbose_name='Territory',null=False)

    def __str__(self):
        return self.officeCode+' > '+self.country