# Generated by Django 4.2.3 on 2023-08-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_dailyentry_remaining_quantity_alter_dailyentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyentry',
            name='remaining_quantity',
            field=models.FloatField(default=0),
        ),
    ]
