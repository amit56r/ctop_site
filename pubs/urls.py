from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.pub_main, name='pub_list'),
    url(r'^page/(?P<pg_id>\d+)/$', views.pub_main, name='pub_with_page')
]