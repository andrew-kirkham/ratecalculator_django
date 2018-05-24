from rest_framework import serializers
from restapi.models import RateRequest

class RateRequestSerializer(serializers.Serializer):
    """Serializer for any incoming rate request
    """

    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
