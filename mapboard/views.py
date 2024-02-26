from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Position

# Create your views here.

def index(request):
    template = loader.get_template("mapboard/index.html")
    context = {
        "body": "body new"
    }
    return HttpResponse(template.render(context, request))


def map(request):
    position_list = [
        {
            "position_name": "test",
            "latitude": -31.91937609059,
            "longitude": 115.7667686476,
            "modified_date": '2023-10-12'
        }
    ]
    try:
        pass
        #position_list = Position.objects.order_by('modified_date')
    except KeyError:
        pass
    
    template = loader.get_template("mapboard/map.html")
    context = {
        "body": "body new",
        "position_list": position_list
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template("mapboard/dashboard.html")
    context = {
        "body": "body new"
    }
    return HttpResponse(template.render(context, request))
