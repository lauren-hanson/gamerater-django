"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gameraterapi.models import Category

class CategoryView(ViewSet): 
    def list(self, request):
        categories = Category.objects.all()
        serialized = CategorySerializer(categories, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        category = Category.objects.get(pk=pk)
        serialized = CategorySerializer(category, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


"""There are 2 ways to do this. You can either add in the extra serializer or add depth = 1 depending on the information you are trying to return. The serializer will help you pick the exact information you want to return while depth will just automatically return all info"""

# class GameCategorySerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model =Category
#         fields = ('id', 'label', )

class CategorySerializer(serializers.ModelSerializer):

    # categories = GameCategorySerializer(many=True)

    """JSON serializer for games"""
    class Meta:
        model = Category
        fields = ('id', 'label', )
        depth = 1

