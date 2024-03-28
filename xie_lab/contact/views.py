from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


def show(request):
    contact = Contact.objects.all()[0]
    context = {"contact": contact}
    return render(request, 'contact/contact.html', context)
