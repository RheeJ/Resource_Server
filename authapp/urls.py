from authapp.views import *
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^print/$', Print_Roles, name="Print_Roles"),
]
