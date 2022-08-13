from django.shortcuts import render, get_object_or_404

# Create your views here.
from contents.models import Content


def home(request, id):
    content = get_object_or_404(Content, pk=id)
    return render(request, 'home.html', context={"content": content})