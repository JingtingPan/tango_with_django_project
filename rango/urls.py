# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:06:34 2024

@author: 10441
"""

from django.urls import path
from rango import views

app_name = "rango"

urlpatterns = [
    path("", views.index, name = "index"),
    ]