from django.db import models


class GameRating(models.Model):

    # 'Player' is referencing the class Player
    # CASCADE delete will make sure that GameRating is deleted if Player(pk) is deleted
    # related_name specifies the name of the reverse relation from the User model back to this model
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player_ratings')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='game_ratings')
    rating = models.IntegerField()
    date_rated = models.DateField()
