import datetime

from django.db import models


class Mastery(models.Model):
    mastery_name = models.CharField(max_length=100, default='Nameless Mastery')
    mastery_description = models.CharField(max_length=200)
    mastery_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.mastery_name

class Comment(models.Model):
    fk_mastery = models.ForeignKey(Mastery, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_votes = models.IntegerField(default=0)

    def commentIsVerified(self):
        if self.comment_votes > 10:
            return True
        return False