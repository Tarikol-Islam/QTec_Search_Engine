# Generated by Django 3.2.7 on 2021-09-06 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_product_product_creation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_pic',
        ),
    ]