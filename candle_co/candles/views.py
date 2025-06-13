from django.shortcuts import render
#import json
#from django.http import HttpResponse
from .models import Candles

# Create your views here.
def index(request):
    return render(request, 'candles/index.html', {
        'candles': Candles.objects.all()
    })
    