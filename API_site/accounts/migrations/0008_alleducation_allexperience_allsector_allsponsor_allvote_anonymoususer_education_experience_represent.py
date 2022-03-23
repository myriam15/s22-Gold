# Generated by Django 3.2.4 on 2022-03-23 23:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220323_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.CharField(max_length=3, null=True, verbose_name='Age')),
                ('zip_code', models.CharField(max_length=12, null=True, verbose_name='ZIP')),
                ('location', models.CharField(max_length=1024, null=True, verbose_name='Location')),
                ('agriculture_and_food', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Agriculture and Food')),
                ('armedforces_and_nationalsecurity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Armed Forces and National Security')),
                ('crime_and_lawenforcement', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Crime and Law Enforcement')),
                ('civilrights_and_liberties_minorityissues', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Civil Rights and Liberties, Minority Issues')),
                ('economics_and_public_finance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Economics and Public Finance')),
                ('education', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Education')),
                ('emergency_management', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Emergency Management')),
                ('environmental_protection', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Environmental Protection')),
                ('governmentoperations_and_politics', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Government Operations and Politics')),
                ('health', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Health')),
                ('immigration', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Immigration')),
                ('internationalaffairs', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='International Affairs')),
                ('labor_and_employment', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Labor and Employment')),
                ('science_technology_communications', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Science, Technology, Communications')),
                ('social_welfare', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Social Welfare')),
                ('taxation', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Taxation')),
                ('transportation_and_public_works', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Transportation and Public Works')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=200, null=True, verbose_name='School Name')),
                ('location', models.CharField(max_length=1024, verbose_name='Location')),
                ('level', models.CharField(max_length=200, null=True, verbose_name='School Name')),
                ('program', models.CharField(max_length=200, null=True, verbose_name='Program')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=200, null=True, verbose_name='Company Name')),
                ('location', models.CharField(max_length=1024, verbose_name='Location')),
                ('type', models.CharField(max_length=200, null=True, verbose_name='Type')),
                ('experienceyear', models.CharField(max_length=3, null=True, verbose_name='Year')),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, null=True, verbose_name='FirstName')),
                ('lastname', models.CharField(max_length=200, null=True, verbose_name='LastName')),
                ('gender', models.CharField(max_length=1, null=True, verbose_name='Gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('homecity', models.CharField(max_length=1024, verbose_name='Home City')),
                ('representativetown', models.CharField(max_length=1024, verbose_name='Representative Town')),
                ('party', models.CharField(max_length=1024, verbose_name='Party')),
                ('agriculture_and_food', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Agriculture and Food')),
                ('armedforces_and_nationalsecurity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Armed Forces and National Security')),
                ('crime_and_lawenforcement', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Crime and Law Enforcement')),
                ('civilrights_and_liberties_minorityissues', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Civil Rights and Liberties, Minority Issues')),
                ('economics_and_public_finance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Economics and Public Finance')),
                ('education', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Education')),
                ('emergency_management', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Emergency Management')),
                ('environmental_protection', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Environmental Protection')),
                ('governmentoperations_and_politics', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Government Operations and Politics')),
                ('health', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Health')),
                ('immigration', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Immigration')),
                ('internationalaffairs', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='International Affairs')),
                ('labor_and_employment', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Labor and Employment')),
                ('science_technology_communications', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Science, Technology, Communications')),
                ('social_welfare', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Social Welfare')),
                ('taxation', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Taxation')),
                ('transportation_and_public_works', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Transportation and Public Works')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=200, null=True, verbose_name='Sector Name')),
                ('amount', models.CharField(max_length=50, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=200, null=True, verbose_name='Organization Name')),
                ('amount', models.CharField(max_length=50, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillNumber', models.CharField(max_length=200, null=True, verbose_name='Company Name')),
                ('Date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('Description', models.CharField(max_length=1024, verbose_name='Location')),
                ('Status', models.CharField(max_length=50, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='Represent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.anonymoususer')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.representative')),
            ],
        ),
        migrations.CreateModel(
            name='AllVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.representative')),
                ('vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.vote')),
            ],
        ),
        migrations.CreateModel(
            name='AllSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.representative')),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='AllSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.representative')),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.sector')),
            ],
        ),
        migrations.CreateModel(
            name='AllExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.experience')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.representative')),
            ],
        ),
        migrations.CreateModel(
            name='AllEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.education')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.representative')),
            ],
        ),
    ]