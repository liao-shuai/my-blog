from django.conf.urls import url
from django.contrib import admin
import blog.views as bv

urlpatterns = [
    url(r'^index/$', bv.index),
   ]
