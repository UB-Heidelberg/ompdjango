# coding: utf-8
# !/usr/bin/env python3
# Created by wit at 15.02.18

from django.urls import path

from heimptui import views

urlpatterns = [
    # heimptui
    path('', views.index, name='index'),
    # heimptui/details/1
    path('<int:submission_id>',  views.detail, name='detail')
    # heimptui/

]
