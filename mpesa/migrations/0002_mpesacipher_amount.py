# Generated by Django 4.0.5 on 2022-09-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesacipher',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
