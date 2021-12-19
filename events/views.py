# Create your views here.
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView 
from django.core.paginator import Paginator
from .modelsP import Page
from .models import Event





class EventList(ListView):
    model = Event

    context_object_name = 'all_events'




class EventView(DetailView):
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event_list'] = Page.objects.all()
        inn = context['event_list']
        
       

        return context

