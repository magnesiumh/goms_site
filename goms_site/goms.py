from django.contrib import admin
from django.urls import path

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('event/', include('events.urls')),
    path('',include('events.urls')),
    path('', include('pages.urls')),
]
