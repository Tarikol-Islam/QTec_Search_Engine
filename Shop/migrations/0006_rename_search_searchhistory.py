# Generated by Django 3.2.7 on 2021-09-07 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20210907_2240'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Search',
            new_name='SearchHistory',
        ),
    ]