# Generated by Django 4.0.5 on 2022-06-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0005_alter_batteryswap_battery_code2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batteryswap',
            name='battery_code2',
        ),
        migrations.AddField(
            model_name='batteryswap',
            name='status',
            field=models.CharField(default='Issued', max_length=50),
        ),
    ]
