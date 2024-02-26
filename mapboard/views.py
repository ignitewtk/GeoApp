from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = loader.get_template("mapboard/index.html")
    context = {
        "body": "body new"
    }
    return HttpResponse(template.render(context, request))


def map(request):
    template = loader.get_template("mapboard/map.html")
    context = {
        "body": "body new"
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template("mapboard/dashboard.html")
    context = {
        "body": "body new"
    }
    return HttpResponse(template.render(context, request))
