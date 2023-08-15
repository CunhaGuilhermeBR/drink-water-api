from django.db import models
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    daily_goal = models.FloatField()

class DailyEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_quantity = models.FloatField(default=0)
    date = models.DateField(default=date.today)
    achieve_goal = models.BooleanField(default=False)
    remaining_quantity = models.FloatField()