# coding: utf-8
# !/usr/bin/env python3
# Created by wit at 15.02.18
from django.contrib import admin
from .models import *
from django.apps import apps


for model in apps.get_app_config('ompdjango').models.values():
    admin.site.register(model)