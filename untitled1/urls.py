# coding:utf-8
"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin 
from my_django import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^show/(\d{4})/(\d{2})/(\d{2})/$',views.showdate),
	url(r'^show1/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',views.showdate,{'home':'index.html'}),     #参数精确匹配，{name:string}为额外的参数
	url(r'^index/',views.index),
	url(r'^dashboard/$',views.bootstrap),
	url(r'^asset/$',views.asset,name='asset'),     #name as alias calling by html file like {% url 'xxxx'%}   in bootstrap.html
	url(r'^host/$',views.host,name='host'),
	url(r'^audit/$',views.audit,name='audit'),
	url(r'^user/$',views.user,name='user'),
	url(r'^$', views.login),
]
