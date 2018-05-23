# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from restapi.models import Rate
from rest_framework import generics
from rest_framework.response import Response
from restapi.serializers import RateListSerializer, RateQuerySerializer, RateRequestSerializer
from rest_framework.views import APIView
from rest_framework import status
from restapi.handlers import RateHandler

# Create your views here.


class RateList(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateListSerializer


class RateQuery(APIView):
    rate_handler = RateHandler()

    def get(self, request, format=None):
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
