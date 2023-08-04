from django.db import models

class Admin(models.Model):
    username=models.CharField(max_length=20,verbose_name='User name',primary_key=True,null=False)
    password=models.CharField(max_length=256,verbose_name='Password',null=False)