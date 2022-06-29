from rest_framework import serializers
from erlangb.models import Erlangb

class ErlangCSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("holdTime", "arrivalRate", "channelNum", "answer")
        model = Erlangb
