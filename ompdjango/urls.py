# coding: utf-8
# !/usr/bin/env python3
# Created by wit at 15.02.18

from django.urls import path
from django.conf import settings
from django.urls import re_path
from django.conf.urls import url
from django.views import static


from ompdjango import views
from ompdjango.views import PressesView

urlpatterns = [
    # ompdjango

    # ompdjango/presses/
    path('', PressesView.as_view()),
    path('presses', PressesView.as_view()),
    # ompdjango/presses/name
    path('press/<int:press_id>/submissions', views.submissions, name='submissions'),
    path('press/<int:press_id>/workflow/<int:submission_id>/<int:stage_id>', views.workflow, name='workflow'),
    # ompdjango/details/1
    path('<int:submission_id>', views.detail, name='press')
    # ompdjango/



]
