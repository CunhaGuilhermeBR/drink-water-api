# Generated by Django 4.2.3 on 2023-08-15 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyentry',
            name='remaining_quantity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailyentry',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
