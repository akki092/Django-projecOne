# -*- coding: utf-8 -*-
from django.conf.urls import url
from projectApp import views

urlpatterns=[
        url('^$',views.extension,name='extension'),]
