# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import markdown
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from markdown.extensions.toc import TocExtension

from blog.models import Post, Category, Tag
from comments.forms import CommentForm

def listing(request):
    contact_list = Post.objecets.all()
    paginator = Paginator(contact_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', context={
        'contacts' : contacts
    })

def index(request):
    # return HttpResponse('欢迎访问我的博客')
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        # 'title' : '我的第一个博客',
        # 'welcome' : '欢迎访问我的博客',
        'post_list' : post_list,
    })

def archives(request, year, month):
    #  下面是双划线__year,注意单划线会报错
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list' : post_list,
    })

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list' : post_list,
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increave_views()
    #  https://www.zmrenwu.com/post/11/
    #  markdown把markdown文本转化成html文本格式
    # 而需要在post.body后面加上safe标签，防止Django转义
    #  body中输入代码时要主要用  英文输入：  ```python ......```（3个~字符）
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.toc',
                                      'markdown.extensions.codehilite',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context=context)


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = u'神仔二弟'
        return render(request, 'blog/index.html', context={'error_msg' : error_msg})

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', context={
        'error_msg' : error_msg,
        'post_list' : post_list,

    })

#  使用基于类的 通用视图 （类视图）

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = list(paginator.page_range)
        #   上面只是上次一个xrange的生成器，所以需要加上list

        if page_number == 1:
            right = page_range[page_number : page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:
            left = page_range[(page_number - 3) if page_number > 3 else 0 : page_number -1]
            if left[0] > 2:
                left_has_more =True
            if left[0] > 1:
                first = True

        else:
            left = page_range[(page_number -3) if page_number > 3 else 0 : page_number -1]
            right = page_range[page_number: page_number + 2]
            if right[-1] < total_pages:
                last = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left' : left,
            'right' : right,
            'left_has_more' : left_has_more,
            'right_has_more' : right_has_more,
            'first' : first,
            'last' : last,
        }
        return data


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk') )
        return super(TagView, self).get_queryset().filter(tags=tag)

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                           created_time__month=month,)


class PostDatialView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDatialView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDatialView, self).get_object(queryset=None)
        """
        post.body = markdown.markdown(post.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.toc',
            'markdown.extensions.codehilite'
        ])
        """
        md = markdown.Markdown(post.body, extensions=[
            'markdown.extensions.extra',
            # 'markdown.extensions.toc',
            TocExtension(slugify=slugify),
            'markdown.extensions.codehilite'
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc

        return post

    def get_context_data(self, **kwargs):
        # post = get_object_or_404(Post, pk = self.kwargs.get('pk'))
        context = super(PostDatialView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            # 'post' : post,
            #  需要将 Markdown 格式的文本渲染成 HTML 文本
            'form' : form,
            'comment_list' : comment_list,
        })
        return context


# Create your views here.
