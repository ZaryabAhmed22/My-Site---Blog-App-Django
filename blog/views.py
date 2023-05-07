from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the home page")


def posts(request):
    return HttpResponse("This page will render all the posts")


def post(request, slug):
    return HttpResponse(f"This page will render the complete post about the {slug}")
