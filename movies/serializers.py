from rest_framework import serializers
from .models import movieData

class movieSerializer(serializers.ModelSerializer):
    image= serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = movieData
        fields = ['id','name','duration','rating','genre','image']
