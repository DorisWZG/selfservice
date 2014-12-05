from django.db import models

# Create your models here.
class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()


class Industry(models.Model):
    IndustryID = models.AutoField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)


class Channel(models.Model):
    ChannelID = models.AutoField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)


class Budget(models.Model):
    BudgetID = models.AutoField(max_length=11, primary_key=True)
    budget = models.CharField(max_length=50)


class PriceMatrix(models.Model):
    PriceMatrixID = models.AutoField(max_length=11, primary_key=True)
    BudgetAllocation = models.DecimalField(decimal_places=10, max_digits=10, max_length=20)
    ExpectedClicks = models.IntegerField(max_length=10)
    CostPerClick = models.DecimalField(decimal_places=10, max_digits=10, max_length=10)
    ExpectedImpressions = models.DecimalField(decimal_places=10, max_digits=10, max_length=50)
    CostPerImpression = models.DecimalField(decimal_places=10, max_digits=10, max_length=10)
    IndustryID = models.ForeignKey(Industry, db_column='IndustryID', max_length=10)
    ChannelID = models.ForeignKey(Channel, db_column='ChannelID', max_length=10)
    BudgetID = models.ForeignKey(Budget, db_column='BudgetID', max_length=10)
