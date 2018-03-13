# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
# from mysite import views as mv
import views

urlpatterns = [
    url(r'^form/$', views.form),
    url(r'^staff/$', views.staff),
    url(r'^templay/$', views.templay),
    url(r'^investigate/$', views.investigate),
]