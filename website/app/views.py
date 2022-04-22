import json.decoder

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from app.models import Lesson, Exercices
from meetings.models import Meeting


def welcome(request):
    return render(request, "app/welcome.html",
                  {
                      "meetings": Meeting.objects.all(),
                      "num_meetings": Meeting.objects.count(),
                      "num_lessons": Lesson.objects.count(),
                      "lessons": Lesson.objects.all(),
                      "num_exercises": Exercices.objects.count()
                  })


def about(request):
    return HttpResponse("This app is an application to learn english phrases")


def phrase(request):
    print(request)
    return HttpResponse("The weather today ___ good.")


def lesson(request, id):
    result_lessons = get_object_or_404(Lesson, pk=id)
    exercises = Exercices.objects.filter(lesson_id=result_lessons.id)
    json_dec = json.decoder.JSONDecoder()
    exercises.sentence = json_dec.dumps(exercises.sentence)
    return render(request, "app/lesson.html", {"lesson": result_lessons, "exercises": exercises})
