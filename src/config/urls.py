from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
VERSION = 'V1.0.0'

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/{}/user/'.format(VERSION),include('app.user.urls',namespace='user')),
    url('api/{}/core/'.format(VERSION),include('app.core.urls',namespace='core')),
    url(r'^docs/', include_docs_urls(title='Docs API USER')),
]
