# Generated by Django 3.1.6 on 2021-02-03 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20210203_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularreport',
            name='employees',
        ),
    ]