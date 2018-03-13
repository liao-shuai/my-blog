#   _*_ coding:utf-8  _*_

from django import template
from django.db.models.aggregates import Count

from blog.models import Post,Category,Tag

register = template.Library()

#  注册这个函数为模板标签
@register.simple_tag()
def get_recent_posts(nums=5):
    return Post.objects.all().order_by('-created_time')[:nums]

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag()
def get_categories():
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    #   gt =  greate than (大于)    gte = greate than equal （大于等于）

@register.simple_tag()
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# @register.simple_tag()
# def get_tags():
#     return Tag.objects.all()