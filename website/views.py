from django.shortcuts import render

# Create your views here.
from .forms import FeedbackCreate


def index(request):
    appis = 0
    if request.method == "POST":
        appis = 1
        form = FeedbackCreate(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'website/index.html', {'form': form, 'appis': appis})
    else:
        form = FeedbackCreate()

    return render(request, 'website/index.html', {'form': form, 'appis': appis})


