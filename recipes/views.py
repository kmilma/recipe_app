# recipes/views.py
from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer
from django.shortcuts import render

# API View
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# Frontend View
def home(request):
    return render(request, 'recipes/index.html')

