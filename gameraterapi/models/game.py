from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    designer = models.CharField(max_length=155)
    year_released = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    num_of_players = models.IntegerField()
    estimated_time = models.FloatField()
    recommended_age = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory")
    

    