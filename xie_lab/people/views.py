from django.http import HttpResponse
from django.shortcuts import render

from .models import Person


def show(request):
    principal = Person.objects.filter(position="0")
    Researchers = Person.objects.filter(position="1")
    PhD = Person.objects.filter(position="2")
    Master = Person.objects.filter(position="3")
    Undergraduate = Person.objects.filter(position="4")
    context = {
        "principal": principal,
        "Researchers": Researchers,
        "PhD": PhD,
        "Master": Master,
        "Undergraduate": Undergraduate
    }
    return render(request, "people/people.html", context)
