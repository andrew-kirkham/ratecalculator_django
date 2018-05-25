# /usr/bin/python
from rest_framework import serializers

class RateRequestSerializer(serializers.Serializer):
    """
    Serializer for any incoming rate request
    """

    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
