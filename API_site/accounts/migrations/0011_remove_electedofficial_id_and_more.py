# Generated by Django 4.0.1 on 2022-03-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_electedofficial_district_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electedofficial',
            name='id',
        ),
        migrations.AlterField(
            model_name='electedofficial',
            name='bioguide_id',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
    ]
