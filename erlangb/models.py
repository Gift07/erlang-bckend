from email.policy import default
from django.db import models


class Erlangb(models.Model):
    holdTime = models.FloatField(default=0)
    arrivalRate = models.FloatField(default=0)
    channelNum = models.FloatField(default=0)
    answer = models.FloatField(default=0)

    def __str__(self):
        return f"erlangb"

