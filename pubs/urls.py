from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.pub_list, name='pub_list'),
]