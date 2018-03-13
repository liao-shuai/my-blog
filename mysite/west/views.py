# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpResponse
from west.models import Character

from west.models import Character

from django import forms


class CharacterForm(forms.Form):
    name = forms.CharField(max_length=200)


def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted = form.cleaned_data['name']
            #  http://www.jb51.net/article/87046.htm  可查看文档
            new_record = Character(name=submitted)
            new_record.save()

    form = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form'] = form
    return render(request, "investigate.html", ctx)

def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)

def staff(request):
    staff_list = Character.objects.all()
    staff_str = map(str, staff_list)

    # context = {'label': ''.join(staff_str)}
    context = {}
    context['label'] = ''.join(staff_str)
    return render(request, 'templay.html', context)

    # return HttpResponse('<p>' + ''.join(staff_str) + '</p>')

# def first_page(requset):
#     return HttpResponse('<p>西餐</p>')

def form(request):
    return render(request, 'form.html')

# def investigate(request):
#     rel = request.get['staff']
#     return HttpResponse(rel)

# def investigate(request):
#     ctx = {}
#     ctx.update(csrf(request))
#     if request.POST:
#         ctx['rel'] = request.POST['staff']
#     return render(request, 'investigate.html', ctx)


# Create your views here.
