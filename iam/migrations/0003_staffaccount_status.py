# Generated by Django 4.0.5 on 2022-07-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iam', '0002_staffaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffaccount',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]
