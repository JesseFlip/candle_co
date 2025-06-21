from django.shortcuts import render
from rest_framework import generics
from .models import CandlePost
from .serializers import CandlePostSerializer

# Create your views here.
class CandlePostListCreate(generics.ListCreateAPIView):
    queryset = CandlePost.objects.all()
    serializer_class = CandlePostSerializer

class CandlePostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandlePost.objects.all()
    serializer_class = CandlePostSerializer
    lookup_field = "pk"