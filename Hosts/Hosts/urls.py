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
    url(r'^host_modify_ajax$', views.host_modify_ajax),
    url(r'^index/', views.index),
    url(r'^business$', views.business),
    url(r'^host', views.host),
    url(r'^test_ajax$', views.test_ajax),
    url(r'^app$', views.app),
    url(r'^ajax_add_app$', views.ajax_add_app),
    url(r'^del_app_ajax$', views.del_app_ajax),
    url(r'^businessdel-(?P<nid>\d+)', views.businessdel),
    url(r'^businessedit-(?P<nid>\d+)', views.businessedit),

    url(r'^del_host_ajax$', views.del_host_ajax),
    url(r'^app_edit_ajax$', views.app_edit_ajax),
    url(r'^login', views.login),
    url(r'^logout', views.logout),
]
