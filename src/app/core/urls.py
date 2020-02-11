from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import api_root, index

app_name = 'core'

urlpatterns = [
    url('api-root/',api_root,name='api_root'),
    url(r'^$', index , name='index'),
]
