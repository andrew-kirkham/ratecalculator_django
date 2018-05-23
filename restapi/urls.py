# /usr/bin/python

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^api/list/$', views.RateList.as_view()),
    url(r'^api/rate/$', views.RateQuery.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
