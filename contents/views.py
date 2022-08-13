from django.shortcuts import render

# Create your views here.
from contents.models import Content


def index(request):
    return render(request, 'home.html')


def concept(request):
    content = Content.objects.get(pk=2)
    return render(request, 'test.html', context={"content": content})


def box(request):
    boxes = Content.objects.get(pk=4)
    return render(request, 'test.html', context={"boxes": boxes})

