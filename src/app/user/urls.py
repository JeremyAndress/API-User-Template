from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from api.user.view import (
    getUsers, getUser,
    signin, user_api_root
)
from api.user.root import user_api_root_detail

app_name = 'user'

urlpatterns = [
    url('user-api-root/',user_api_root,name='user_api_root'),
    url('user-api-root-detail/',user_api_root_detail,name='user_api_root_detail'),
    url('getUsers/',getUsers,name='getUsers'),
    url('getUser',getUser,name='getUser'),
    url('signin',signin,name='signin'),
]
