# Generated by Django 3.2 on 2021-06-18 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0020_auto_20210618_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehousestaff',
            name='import_file',
        ),
    ]
