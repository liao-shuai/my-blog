#  -*_ coding:utf-8 _*_

from django.conf.urls import url
from django.contrib import admin

from comments import views

app_name = 'comments'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # # url(r'^post/(?p<pk>[0-9]+)/$', views.detail, name='detail'),
    # #  P要大写，不然会匹配不到
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]

