from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
    url(r'^populate$', views.populate),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^removethis/(?P<id>\d+)$', views.removethis),
]
