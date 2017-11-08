"""Hosts URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from Management import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #主页
    url(r'^index/', views.index),
    #业务线
    url(r'^business$', views.business),
    #业务线删除
    url(r'^businessdel-(?P<nid>\d+)', views.businessdel),
    #业务线修改
    url(r'^businessedit-(?P<nid>\d+)', views.businessedit),

    #主机修改,注意和host的顺序！！！
    url(r'^host_modify_ajax$', views.host_modify_ajax),
    #主机
    url(r'^host', views.host),
    #主机删除
    url(r'^del_host_ajax$', views.del_host_ajax),
    #主机添加
    url(r'^test_ajax$', views.test_ajax),

    #app
    url(r'^app', views.app),
    #app添加
    url(r'^ajax_add_app$', views.ajax_add_app),
    #app删除
    url(r'^del_app_ajax$', views.del_app_ajax),
    #app修改
    url(r'^app_edit_ajax$', views.app_edit_ajax),

    #登录
    url(r'^login', views.login),
    #注销
    url(r'^logout', views.logout),
]
