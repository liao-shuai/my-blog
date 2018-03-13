# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Character, Contact, Tag
# from django.db import models

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    list_display = ('name', 'age', 'email')
    fieldsets = (
        ['Main', {
            'fields' : ('name', 'email'),
                  }],
        ['Advance', {
            'classes' : ('collapse'),
            'fields' : ('age',),   # age后面必须要带逗号，不然会出错
        }]
    )
admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
  # usename: villa    password: liaoshuai (数字不行，8个字节符号)
# Register your models here.
