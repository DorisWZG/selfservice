from django.db import models

# Create your models here.

class Industry(models.Model):
    industryID = models.AutoField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)


class Channel(models.Model):
    channelID = models.AutoField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)


class PriceMatrix(models.Model):
    priceMatrixID = models.AutoField(max_length=11, primary_key=True)
    allocation = models.FloatField()
    budget = models.FloatField()
    expectedClicks = models.IntegerField()
    costPerClick = models.FloatField()
    expectedImpressions = models.FloatField()
    costPerImpression = models.FloatField()
    industryID = models.ForeignKey(Industry, db_column='industryID', max_length=10)
    channelID = models.ForeignKey(Channel, db_column='channelID', max_length=10)