from django.forms import widgets


from rest_framework import serializers

from restapi.models import Task, Channel, Industry, Budget, PriceMatrix


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('ChannelID', 'name')

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('IndustryID','name')

class BudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Budget
        fields = ('BudgetID', 'budget')

class PriceMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceMatrix
        fields = ('PriceMatrixID','BudgetAllocation','ExpectedClicks','CostPerClick','ExpectedImpressions','CostPerImpression','IndustryID','ChannelID','BudgetID')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')