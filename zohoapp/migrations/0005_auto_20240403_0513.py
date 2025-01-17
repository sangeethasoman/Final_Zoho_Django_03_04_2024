# Generated by Django 3.2.25 on 2024-04-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0004_auto_20240403_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='acc_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='bill_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='cheque',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='paid',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='payment_methode',
            field=models.CharField(blank=True, default='Cash', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='shipping_charge',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='status',
            field=models.CharField(default='Draft', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='upi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
