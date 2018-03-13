# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post, Tag, Category

#  定制admin
class PostAdmin1(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time', 'modified_time',  'category']

class PostAdmin2(admin.ModelAdmin):
    list_display = ['name']

class PostAdmin3(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, PostAdmin1)
admin.site.register(Tag, PostAdmin3)
admin.site.register(Category, PostAdmin2)
# Register your models here.
