"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gameraterapi.models import Game, GameCategory, Category

class GameView(ViewSet): 
    def list(self, request):
        games = Game.objects.all()
        serialized = GameSerializer(games, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serialized = GameSerializer(game, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request): 
        new_game = Game()
        # [] property is coming from client side 
        # assigning properties
        new_game.description = request.data['description']
        new_game.designer = request.data['designer']
        new_game.estimated_time = request.data['time']
        new_game.title = request.data['title']
        new_game.min_players = request.data['min_players']
        new_game.max_players = request.data['max_players']
        new_game.save()
        
        categories_selected = request.data['catagories']

        for category in categories_selected: 
            relationship = GameCategory()
            relationship.game = new_game
            relationship.category = Category.objects.get(pk = category)
            relationship.save()

        serializer = GameSerializer(new_game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



"""There are 2 ways to do this. You can either add in the extra serializer or add depth = 1 depending on the information you are trying to return. The serializer will help you pick the exact information you want to return while depth will just automatically return all info"""

# class GameCategorySerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model =Category
#         fields = ('id', 'label', )

class GameSerializer(serializers.ModelSerializer):

    # categories = GameCategorySerializer(many=True)

    """JSON serializer for games"""
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'min_players', 'max_players', 'estimated_time', 'recommended_age', 'categories', )
        depth = 1

