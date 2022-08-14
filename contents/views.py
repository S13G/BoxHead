from django.shortcuts import render

# Create your views here.
from contents.models import Content


def concept(request):
    content = Content.objects.get(pk=1)
    return render(request, 'index.html', context={"concept": content})


def box_house(request):
    boxes = Content.objects.get(pk=2)
    return render(request, 'box_house.html', context={"boxes": boxes})


def short_term(request):
    shorts = Content.objects.get(pk=3)
    return render(request, 'short_term.html', context={"shorts": shorts})


def long_term(request):
    long = Content.objects.get(pk=4)
    return render(request, 'long_term.html', context={"long": long})


def box_map(request):
    return render(request, 'box_map.html')