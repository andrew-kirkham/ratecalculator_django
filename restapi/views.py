# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from restapi.serializers import RateRequestSerializer
from rest_framework.views import APIView
from rest_framework import status
from restapi.rate_handler import RateHandler
from restapi.config import config
from rest_framework.compat import coreschema
from rest_framework.schemas import AutoSchema
from coreapi import Field


class RateList(APIView):
    def get(self, request, format=None):
        """Get all the rates configured

        Arguments:
            APIView {APIView} -- [description]
            request {request} -- the HTTP request

        Keyword Arguments:
            format {format} -- Format to return the rates in (default: {None})

        Returns:
            Response -- a Response containing the configured rates
        """

        return Response(config)

class RateQuery(APIView):
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

    def get(self, request, format=None):
        """Get the rate for a given date range

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

        return self._handle_request(request.query_params)

    def post(self, request, format=None):
        return self._handle_request(request.data)

    def _handle_request(self, data):
        serializer = RateRequestSerializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_time = serializer.validated_data['start']
        end_time = serializer.validated_data['end']
        return self.rate_handler.handle_request(start_time, end_time)
