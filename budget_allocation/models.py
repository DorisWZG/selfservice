
from django.db import models

# Create your models here.

class Industry(models.Model):
    industryId = models.AutoField(max_length=11, primary_key=True)
    industryName = models.CharField(max_length=100)


class Channel(models.Model):
    channelId = models.AutoField(max_length=11, primary_key=True)
    channelName = models.CharField(max_length=100)
    minMediaBuy = models.IntegerField(null=True)


class PriceMetrics(models.Model):
    priceMatrixId = models.AutoField(max_length=11, primary_key=True)
    allocation = models.FloatField()
    budget = models.FloatField()
    expectedClicks = models.IntegerField()
    costPerClick = models.FloatField()
    expectedImpressions = models.FloatField()
    costPerImpression = models.FloatField()
    industryId = models.ForeignKey(Industry, db_column='industryId', max_length=10)
    channelId = models.ForeignKey(Channel, db_column='channelId', max_length=10)
