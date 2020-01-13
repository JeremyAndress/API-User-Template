from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from api.user.view import (
    getUsers, user_api_root, getUser
)

app_name = 'user'

urlpatterns = [
    url('user-api-root/',user_api_root,name='user_api_root'),
    url('getUsers/',getUsers,name='getUsers'),
    url(r'getUser/(?P<pk>\d+)/$',getUser,name='getUser'),
]
