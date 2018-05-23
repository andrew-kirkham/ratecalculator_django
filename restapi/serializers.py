from rest_framework import serializers
from restapi.models import Rate, RateRequest

class RateQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('price',)

class RateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('days', 'times', 'price')

class RateRequestSerializer(serializers.Serializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
