from django.shortcuts import render 
from django.views.generic import View
from .models import Vids




# Create your views here.
def uservices(request):
    
    #vd = Vids.objects.filter(Vids)
    context = {'vids_list':Vids.objects.all(),}
    return render(request, 'pservices.html', context)