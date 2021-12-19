
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('event/', include('events.urls')),
    #path("", include('events.urls')),
    path('uservices/',include('Uservices.urls')),
    
    #path('event/uservices/uservices/', include('Uservices.urls')),
    
    path('', include('pages.urls')),
]
