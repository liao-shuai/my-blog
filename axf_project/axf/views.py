# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'axf/home.html', context={
        'title': '主页',
    })

def market(request):
    return render(request, 'axf/market.html', context={
        'title': '闪送超市',
    })

def cart(request):
    return render(request, 'axf/cart.html', context={
        'title': '购物车',

    })

def mine(request):
    return render(request, 'axf/mine.html', context={
        'title': '我的',

    })


# Create your views here.
