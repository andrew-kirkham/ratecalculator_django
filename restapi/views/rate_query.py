# /usr/bin/python
from __future__ import unicode_literals

from coreapi import Field
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.compat import coreschema
from rest_framework.schemas import AutoSchema
from rest_framework.parsers import JSONParser
from rest_framework_xml.parsers import XMLParser
from restapi.serializers.rate_request_serializer import RateRequestSerializer
from restapi.rate_handler import RateHandler


class RateQuery(APIView):
    parser_classes = (JSONParser, XMLParser)
    schema = AutoSchema(manual_fields=[
        Field(
            "start",
            required=True,
            schema=coreschema.String()
        ),
        Field(
            "end",
            required=True,
            schema=coreschema.String()
        )
    ])
    rate_handler = RateHandler()

    def get(self, request):
        """Get the rate for a given date range
        This is the GET version which accepts query params

        Arguments:
            request {[type]} -- [description]

        Returns:
            integer -- the rate for the given range

        Responses:
            200 -- OK
            404 -- No rate found for range
        """

        return self._handle_request(request.query_params)

    def post(self, request):
        """Get the rate for a given date range
        This is the POST equivalent that accepts a json/xml format

        Arguments:
            request {[type]} -- [description]

        Keyword Arguments:
            format {[type]} -- [description] (default: {None})

        Returns:
            integer -- the rate for the given range

        Responses:
            200 -- OK
            404 -- No rate found for range
        """
        return self._handle_request(request.data)

    def _handle_request(self, data):
        serializer = RateRequestSerializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_time = serializer.validated_data['start']
        end_time = serializer.validated_data['end']
        return self.rate_handler.handle_request(start_time, end_time)
