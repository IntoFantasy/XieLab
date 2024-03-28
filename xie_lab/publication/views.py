from django.http import HttpResponse
from django.shortcuts import render
from .models import Publication


def show(request):
    articles_list = Publication.objects.order_by('-pub_year')
    context = {'articles_list': articles_list}
    return render(request, "publication/publication.html", context)
