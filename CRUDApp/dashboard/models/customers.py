from django.db import models
from .employees import Employees
class Customers(models.Model):
    customerNumber=models.PositiveIntegerField(verbose_name='Customer Number',null=False,primary_key=True)
    customerName=models.CharField(max_length=50,verbose_name='Customer Name',null=False)
    contactLastName=models.CharField(max_length=50,verbose_name='Contact Last Name',null=False)
    contactFirstName=models.CharField(max_length=50,verbose_name='Contact First Name',null=False)
    phone=models.CharField(max_length=50,verbose_name='Phone',null=False)
    addressLine1=models.CharField(max_length=50,verbose_name='Address Line 1',null=False)
    addressLine2=models.CharField(max_length=50,verbose_name='Address Line 2',null=True,default=None)
    city=models.CharField(max_length=50,verbose_name='City',null=False)
    state=models.CharField(max_length=50,verbose_name='State',null=True,default=None)
    postalCode=models.CharField(max_length=15,verbose_name='Postal Code',null=True,default=None)
    country=models.CharField(max_length=50,verbose_name='Country',null=False)
    salesRepEmployeeNumber=models.ForeignKey(Employees,on_delete=models.RESTRICT,verbose_name='Sales Rep Employee Number',null=True,default=None)
    creditLimit=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Credit Limit',null=True,default=None)

    def __str__(self):
        return self.customerName+'->'+str(self.customerNumber)
