from django.db import models

class Productlines(models.Model):
    productLine=models.CharField(max_length=50,verbose_name='Product Line',null=False,primary_key=True)
    textDescription=models.TextField(verbose_name='Text Description',null=True,default=None)

    def __str__(self):
        return self.productLine

