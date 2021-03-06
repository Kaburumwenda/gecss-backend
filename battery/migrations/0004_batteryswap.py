# Generated by Django 4.0.5 on 2022-06-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0003_batterystation_status_alter_batterystation_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatterySwap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_no', models.CharField(max_length=150)),
                ('mem_no', models.CharField(max_length=100)),
                ('battery_code1', models.CharField(max_length=30)),
                ('battery_code2', models.CharField(default='Active', max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
