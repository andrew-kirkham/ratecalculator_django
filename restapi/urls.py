# /usr/bin/python
"""URLs - router for all urls in this application
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from restapi import views

schema_view = get_swagger_view(title='Coding Challenge')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/list/$', views.RateList.as_view()),
    url(r'^api/rate/$', views.RateQuery.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
