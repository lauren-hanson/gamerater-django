from django.db import models

class GameReview(models.Model): 
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='players')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='games')
    rating = models.IntegerField()
    date_reviewed = models.DateField()