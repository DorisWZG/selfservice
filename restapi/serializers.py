from django.forms import widgets

from rest_framework import serializers
from restapi.models import  Channel, Industry, PriceMatrix


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('channelID', 'name')


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('industryID', 'name')



class PriceMatrixSerializer(serializers.ModelSerializer):
    # serializers.IntegerField(max_value=None)
    # serializers.DecimalField(max_digits=10, decimal_places=10)
    class Meta:
        model = PriceMatrix
        fields = ('priceMatrixID', 'allocation', 'budget', 'expectedClicks','costPerClick','expectedImpressions','costPerImpression','industryID','channelID')

