# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from restapi.models import Rate
from rest_framework import generics
from rest_framework.response import Response
from restapi.serializers import RateListSerializer, RateQuerySerializer, RateRequestSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class RateList(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateListSerializer


class RateQuery(APIView):
    def get(self, request, format=None):
        #validate that the query params are date time
        qps = RateRequestSerializer(data=request.query_params)
        print qps.is_valid()
        if not qps.is_valid():
            return Response(data=qps.errors, status=status.HTTP_400_BAD_REQUEST)

        print qps.data
        rate = Rate.objects.get(pk=1)
        serializer = RateQuerySerializer(rate)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RateRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("donezo")
