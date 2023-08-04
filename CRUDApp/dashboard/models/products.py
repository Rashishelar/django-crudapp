from django.db import models
from .productlines import Productlines
from .orders import Orders
class Products(models.Model):
    productCode=models.CharField(max_length=15,verbose_name='Product Code',null=False,primary_key=True)
    productName=models.CharField(max_length=70,verbose_name='Product Name',null=False)
    productLine=models.ForeignKey(Productlines,on_delete=models.RESTRICT,null=False,verbose_name='Product Line')
    productScale=models.CharField(max_length=10,verbose_name='Product Scale',null=False)
    productVendor=models.CharField(max_length=50,verbose_name='Product Vendor',null=False)
    productDescription=models.TextField(verbose_name='Product Description',null=False)
    quantityInStock=models.PositiveSmallIntegerField(verbose_name='Quantity In Stock',null=False)
    buyPrice=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Buy Price',null=False)
    MSRP=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='MSRP',null=False)
    orderNumber=models.ManyToManyField(Orders,verbose_name='Order Number',through='Orderdetails')

    def __str__(self) :
        return self.productCode+' > '+self.productName
    