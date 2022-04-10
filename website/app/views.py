from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def welcome(request):
    return HttpResponse("Willkommen App test <a href=/admin>admin</a>")


def about(request):
    return HttpResponse("This app is an application to learn english phrases")


def phrase(request):
    print(request)
    return HttpResponse("The weather today ___ good.")
