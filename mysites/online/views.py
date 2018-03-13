# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from online.models import User

# 表单
class UserForm(forms.Form):
    username = forms.CharField(max_length=50, label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

# 注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponse('regist success!')
    else:
        uf = UserForm()
    return render(request, 'regist.html', context={'uf': uf})

#  登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #  获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username, password__exact = password)
            # user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3360)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
        return render(request, 'login.html', {'uf': uf})

#  登录成功
def index(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'index.html', {'username': username })

#  退出
def logout(request):
    response = HttpResponse('logout!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return response


# Create your views here.
