#  _*_  coding:utf-8  _*_
from django.contrib.syndication.views import Feed

from blog.models import Post

class AllPostRssFeed(Feed):
    title = 'django 博客教程演示项目'
    description = 'django 测试文章'
    link = 'http://127.0.0.1:8000/all/rss/'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s ' % (item.category, item.title)

    def item_description(self, item):
        return item.body