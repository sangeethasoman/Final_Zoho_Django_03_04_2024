# Generated by Django 3.2.25 on 2024-04-03 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverychellan',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='deliverychellan',
            name='to_inv',
        ),
        migrations.RemoveField(
            model_name='deliverychellan',
            name='to_recinv',
        ),
    ]
