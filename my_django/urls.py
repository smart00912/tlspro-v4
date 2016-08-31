# coding:utf-8
from django.conf.urls import url
from django.contrib import admin 
from my_django import views

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#	url(r'^show/(\d{4})/(\d{2})/(\d{2})/$',views.showdate),
#	url(r'^show1/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',views.showdate,{'home':'index.html'}),     #参数精确匹配，{name:string}为额外的参数
#	url(r'^index/',views.index),
	url(r'^dashboard/$',views.bootstrap,name='dashboard'),
	url(r'^asset/$',views.asset,name='asset'),     #name as alias calling by html file like {% url 'xxxx'%}   in bootstrap.html
	url(r'^host/$',views.host,name='host'),
	url(r'^audit/$',views.audit,name='audit'),
	url(r'^user/$',views.user,name='user'),
    url(r'^syslog/$',views.syslog,name='syslog'),
	url(r'^userlog/$',views.userlog,name='userlog'),
	url(r'^upload/$',views.upload,name='upload'),
	url(r'^adm/$',views.adm,name='adm'),
	url(r'^$', views.acc_login,name='login'),
	url(r'^logout/$', views.acc_logout,name='logout'),
]

#link check        
# http://blog.csdn.net/feng88724/article/details/7262514
# http://blog.csdn.net/wcc526/article/details/14458641
