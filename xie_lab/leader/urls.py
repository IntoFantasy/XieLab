from django.urls import path

from . import views

app_name = 'leader'
urlpatterns = [
    path("", views.show, name="index"),
]