from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def show(request):
    news_list = News.objects.order_by('-date')[:3]
    context = {'news_list': news_list}
    return render(request, "homepage/homepage.html", context)
