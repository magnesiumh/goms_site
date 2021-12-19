from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
from .models import Page


def index(request, pagename):
    pagename = "/" + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {'title': pg.title,
               'content': pg.bodytext,
               'last_updated': pg.update_date,
               'page_list': Page.objects.all(), }
    # assert False
    return render(request, 'pages/page.html', context)

