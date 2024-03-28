from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls import re_path
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('publication', include('publication.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('people', include('people.urls')),
    path('research', include('research.urls')),
    path('contact', include('contact.urls')),
    path('leader', include('leader.urls'))
]

