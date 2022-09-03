from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello Bishal")

# Create your views here.
