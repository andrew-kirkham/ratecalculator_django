# /usr/bin/python
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.config import config


class RateList(APIView):
    def get(self, request):
        """Get all the rates configured

        Arguments:
            request {request} -- the HTTP request

        Keyword Arguments:
            format {format} -- Format to return the rates in (default: {None})

        Returns:
            Response -- a Response containing the configured rates
        """

        return Response(config)
