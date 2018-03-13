# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'text', 'post', 'created_time']

from comments.models import Comment

admin.site.register(Comment, CommentAdmin)
# Register your models here.
