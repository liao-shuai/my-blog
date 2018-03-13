# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags


class Category(models.Model):
    name = models.CharField(max_length=120)

class Tag(models.Model):
    name = models.CharField(max_length=120)

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    body = models.TextField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)


    #   或者直接用 {{ post.body | truncatechars : 54 }}
    #  缺点就是如果前 54 个字符含有块级 HTML 元素标签的话
    # （比如一段代码块），会使摘要比较难看。所以推荐使用第一种方法
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(
                extensions = [
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
 # Create your models here.
