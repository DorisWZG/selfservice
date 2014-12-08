from django.forms import widgets

from rest_framework import serializers
from budget_allocation.models import  Channel, Industry, PriceMetrics


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('channelId', 'channelName')


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('industryId', 'industryName')



class PriceMetricsSerializer(serializers.ModelSerializer):
    # serializers.IntegerField(max_value=None)
    # serializers.DecimalField(max_digits=10, decimal_places=10)
    class Meta:
        model = PriceMetrics
        fields = ('priceMatrixId', 'allocation', 'budget', 'expectedClicks','costPerClick','expectedImpressions','costPerImpression','industryId','channelId')

