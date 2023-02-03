from django.db import models


class Player(models.Model):
    biography = models.CharField(max_length=500)
    days_available = models.CharField(max_length=250)
