from django.db import models
from datetime import datetime

# Create your models here.
class Date(models.Model):
    date = models.DateField(primary_key=True)
    month = models.IntegerField()
    year = models.IntegerField()
    month_year = models.CharField(max_length=10)
    semester = models.IntegerField()
    trimester = models.IntegerField()
    quartile = models.IntegerField()

    def __str__(self):
        return (self.date.strftime("%d/%m/%Y")) 