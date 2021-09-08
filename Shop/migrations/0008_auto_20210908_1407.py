# Generated by Django 3.2.7 on 2021-09-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_auto_20210908_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_Qty',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_creation_time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=0, null=True),
        ),
    ]
