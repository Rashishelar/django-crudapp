from django.db import models
from .orders import Orders
from .products import Products

class Orderdetails(models.Model):
    orderNumber=models.ForeignKey(Orders,on_delete=models.RESTRICT,verbose_name='Order Number',null=False)
    productCode=models.ForeignKey(Products,on_delete=models.RESTRICT,verbose_name='Product Code',null=False)
    quantityOrdered=models.PositiveIntegerField(verbose_name='Quantity Ordered',null=False)
    priceEach=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Price Each',null=False)
    orderLineNumber=models.PositiveSmallIntegerField(verbose_name='Order Line Number',null=False)

    