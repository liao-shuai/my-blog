# -*- coding: utf-8 -*-

from django.http import HttpResponse

def first_page(requset):
    return HttpResponse('<p>世界好</p>')