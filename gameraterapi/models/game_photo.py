from django.db import models


class GamePhoto(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='games')
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='players')
    photo_url = models.CharField(max_length = 155)
    