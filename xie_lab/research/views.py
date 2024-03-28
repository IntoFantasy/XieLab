from django.http import HttpResponse
from django.shortcuts import render
from .models import Research, Abstract


def show(request):
    abstract = Abstract.objects.all()[0]
    researches = Research.objects.order_by('order')
    context = {'abstract': abstract, 'researches': researches}
    return render(request, 'research/research.html', context)
