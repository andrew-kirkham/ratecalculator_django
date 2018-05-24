from rest_framework import serializers
from restapi.models import RateRequest

class RateRequestSerializer(serializers.Serializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
