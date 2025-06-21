from rest_framework import serializers
from .models import CandlePost

class CandlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandlePost
        fields = ['id','name', 'scent', 'price', 'inventory']