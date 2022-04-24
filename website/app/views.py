from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from app.models import Lesson, Exercice


def welcome(request):
    return render(request, "app/welcome.html",
                  {
                      "num_lessons": Lesson.objects.count(),
                      "lessons": Lesson.objects.all(),
                      "num_exercises": Exercice.objects.count()
                  })


def about(request):
    return HttpResponse("This app is an application to learn english phrases")


def phrase(request):
    print(request)
    return HttpResponse("The weather today ___ good.")


def lesson(request, id):
    result_lessons = get_object_or_404(Lesson, pk=id)
    exercises = Exercice.objects.filter(lesson_id=result_lessons.id)
    sentences = []
    for ex in list(exercises.all()):
        sentences = ex.sentence.split(';')
        ex.sentence = sentences

    # exercises.sentence = json_dec.dumps(exercises.sentence)
    return render(request, "app/lesson.html",
                  {"lesson": result_lessons, "exercises": exercises, "sentences": sentences})
