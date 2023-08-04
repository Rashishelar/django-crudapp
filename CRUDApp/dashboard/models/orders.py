from django.db import models
from .customers import Customers
class Orders(models.Model):
    orderNumber=models.PositiveIntegerField(verbose_name='Order Number',null=False,primary_key=True)
    orderDate=models.DateField(auto_now=False,auto_now_add=False,verbose_name='Order Date',null=False)
    requiredDate=models.DateField(auto_now=False,auto_now_add=False,verbose_name='Required Date',null=False)
    shippedDate=models.DateField(auto_now=False,auto_now_add=False,verbose_name='Shipped Date',null=True,default=None)
    status=models.CharField(max_length=15,verbose_name='Status',null=False)
    comments=models.TextField(verbose_name='Comments',null=True)
    customerNumber=models.ForeignKey(Customers,on_delete=models.RESTRICT,verbose_name='Customer Number')

    def __str__(self):
        return str(self.orderNumber)+' > '+self.customerNumber.customerName
    