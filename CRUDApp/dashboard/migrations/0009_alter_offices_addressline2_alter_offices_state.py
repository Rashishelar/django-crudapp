# Generated by Django 4.2.3 on 2023-07-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offices',
            name='addressLine2',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='offices',
            name='state',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='State'),
        ),
    ]