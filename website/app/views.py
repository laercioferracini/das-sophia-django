from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404


# Create your views here.
from app.models import Lesson, Phrases
from meetings.models import Meeting


def welcome(request):
    return render(request, "app/welcome.html",
                  {"num_meetings": Meeting.objects.count(),
                   "num_lessons": Lesson.objects.count(),
                   "num_exercises": Phrases.objects.count()})


def about(request):
    return HttpResponse("This app is an application to learn english phrases")


def phrase(request):
    print(request)
    return HttpResponse("The weather today ___ good.")


def lessons(request, id):
    lesson = get_object_or_404(Lesson, pk=id)
    return render(request, "app/lessons.html", {"lesson": lesson})

