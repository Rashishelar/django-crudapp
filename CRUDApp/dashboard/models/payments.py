from django.db import models
from .customers import Customers
from .orders import Orders
class Payments(models.Model):
    paymentID=models.PositiveIntegerField(verbose_name='Payment ID',null=False,primary_key=True)
    customerNumber=models.ForeignKey(Customers,on_delete=models.RESTRICT,verbose_name='Customer Number',null=False)
    orderNumber=models.ForeignKey(Orders,on_delete=models.RESTRICT,verbose_name='Order Number',null=False)
    paymentDate=models.DateField(auto_now=False,auto_now_add=False,verbose_name='Payment Date',null=False)
    totalAmount=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Total Amount',null=False)

    def __str__(self):
        return self.paymentID
