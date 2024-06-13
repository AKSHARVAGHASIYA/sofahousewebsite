# Generated by Django 5.0.6 on 2024-05-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_countryname', models.CharField(max_length=50)),
                ('c_fname', models.CharField(max_length=50)),
                ('c_lname', models.CharField(max_length=50)),
                ('c_companyname', models.CharField(max_length=50)),
                ('c_address', models.CharField(max_length=100)),
                ('c_full_address', models.CharField(max_length=150)),
                ('c_state_country', models.CharField(max_length=50)),
                ('c_email', models.EmailField(max_length=254)),
                ('c_phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]
