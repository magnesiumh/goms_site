from django.urls import path

from . import views
from .views import EventList, EventView



urlpatterns = [
    path('open', EventList.as_view(), name='show-eventz'),
    path('', EventList.as_view(), name='show-eventz'),
    path('show/<int:pk>', EventView.as_view(), name='show-events'),
    path('', EventView.as_view(), name='show-events'),
   # path('', views.index, {'pagename': ''}, name='home'),
    #path('show', EventView.as_view(), name='show-quotes'),
]
