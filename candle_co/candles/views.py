#from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        "candle_1": {
            "name": "Cool Breeze",
            "price": 14.99,
            "scent": "mint",
            "category": "refreshing"
        },
        "candle_2": {
            "name": "Salted Amber",
            "price": 14.99,
            "scent": "Amber",
            "category": "invigorating"
        },
        "candle_3": {
            "name": "Cocoa Butter",
            "price": 14.99,
            "scent": "Cocoa Butter",
            "Category": "natural"
        } 
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    return response