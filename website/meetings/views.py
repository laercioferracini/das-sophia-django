from django.shortcuts import render, get_object_or_404, redirect

from .forms import MeetingForm
# Create your views here.
from .models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


def meetings(request):
    return render(request, "meetings/meetings.html", {
        "meetings": Meeting.objects.all(),
        "num_meetings": Meeting.objects.count()
    })
