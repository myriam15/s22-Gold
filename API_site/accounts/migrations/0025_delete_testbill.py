# Generated by Django 4.0.1 on 2022-04-06 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_rename_committee_1_testbill_chamber_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestBill',
        ),
    ]
