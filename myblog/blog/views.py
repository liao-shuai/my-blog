# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import models
from models import Artical

def hello(request):
    now = datetime.datetime.now()
    html = '<html><body><h3>Hello World</h3>It is now %s</body></html>' % now
    return HttpResponse(html)

def index(request):
    # artical = models.Artical.objects.get(pk=1)
    context = {}
    context['artical'] = 'Hello, Blog'
    return render(request, 'index.html', context)
# Create your views here.
