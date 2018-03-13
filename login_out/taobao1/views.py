# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import time

from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)

#注册
# @csrf_exempt
def register(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # # 判断用户是否存在
            # user = auth.authenticate(username = username,password = password)
            # if user:
            #     context['userExit']=True
            #     return render(req, 'register.html', context)

            #添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login = now_time
            user.save()

            #添加到session
            req.session['username'] = username
            #调用auth登录
            auth.login(req, user)
            #重定向到首页
            return HttpResponse('register success !')
    else:
        context = {'isLogin':False}
    #将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return  render(req,'register.html',context)

#登陆
# @csrf_exempt
def login(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #获取的表单数据与数据库进行比较
            user = auth.authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(req,user)
                req.session['username'] = username
                return HttpResponseRedirect('/taobao1/')
            else:
                #比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(req, 'login.html', context)
    else:
        context = {'isLogin': False,'pswd':True}
    return render(req, 'login.html', context)

#  登录成功
def index(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'index.html', {'username': username })

#登出
def logout(req):
    #清理cookie里保存username
    auth.logout(req)
    return HttpResponse('bye')
# Create your views here.
