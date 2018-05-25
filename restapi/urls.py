# /usr/bin/python
"""URLs - router for all urls in this application
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from restapi.views.rate_list import RateList
from restapi.views.rate_query import RateQuery

schema_view = get_swagger_view(title='Coding Challenge')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/list/$', RateList.as_view()),
    url(r'^api/rate/$', RateQuery.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
