from django.shortcuts import render
from rest_framework import viewsets
from .serializers import movieSerializer
from .models import movieData

# Create your views here.

class movieViewSet(viewsets.ModelViewSet):
    queryset= movieData.objects.all()
    serializer_class=movieSerializer

class genreActionViewSet(viewsets.ModelViewSet):
    queryset= movieData.objects.filter(genre='action')
    serializer_class=movieSerializer

class genreComedyViewSet(viewsets.ModelViewSet):
    queryset= movieData.objects.filter(genre='Comedy')
    serializer_class=movieSerializer