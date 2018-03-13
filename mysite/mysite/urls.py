#   _*_  coding:utf-8  _*_
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from mysite import views as mv
import views
# from views import form

import west
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.first_page),
    url(r'^west/$', include('west.urls')),
    #  这里后面带$没有关系，但是其他情况下不能带$结尾
    url(r'^west/$', include('west.urls')),
    url(r'^west/', include('west.urls')),
    url(r'^west/', include('west.urls')),
]



#   http://blog.csdn.net/u010278162/article/details/52159738
#    根据上个这个链接，include方法一个就够了，不需要重复使用
#   （上面这话有错，实践证明不能少）
