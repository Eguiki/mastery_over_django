import datetime

from django.db import models


class Mastery(models.Model):
    mastery_name = models.CharField(max_length=100, default='Nameless Mastery')
    mastery_description = models.CharField(max_length=200)
    mastery_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.mastery_name
