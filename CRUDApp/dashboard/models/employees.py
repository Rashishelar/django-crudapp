from django.db import models
from .offices import Offices
class Employees(models.Model):
    employeeNumber=models.PositiveIntegerField(verbose_name='Employee Number',null=False,primary_key=True)
    lastName=models.CharField(max_length=50,verbose_name='Last Name',null=False)
    firstName=models.CharField(max_length=50,verbose_name='First Name',null=False)
    extension=models.CharField(max_length=10,verbose_name='Extension',null=False)
    email=models.EmailField(max_length=100,verbose_name='Email',null=False)
    officeCode=models.ForeignKey(Offices,verbose_name='Office Code',on_delete=models.CASCADE,null=False)
    reportsTo=models.ForeignKey('self',verbose_name='reportsTo',on_delete=models.RESTRICT,default=None,null=True)
    jobTitle=models.CharField(max_length=50,verbose_name='Job Title',null=False)
    
    def __str__(self):
        return self.firstName+' '+self.lastName+'->'+str(self.employeeNumber)
 
    
