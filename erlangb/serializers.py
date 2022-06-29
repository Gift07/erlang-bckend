from rest_framework import serializers
from .models import Erlangb

class ErlangBSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("holdTime", "arrivalRate", "channelNum", "answer")
        model = Erlangb
