# from __future__ import unicode_literals
# from django.db import models
#
# # Create your models here.
# class Channel(models.Model):
#     channelid = models.IntegerField(primary_key=True)
#     channelname = models.CharField(max_length=50)
#     min_media_buy = models.IntegerField(blank=True, null=True)
#     localname = models.CharField(max_length=50, blank=True)
#     category = models.CharField(max_length=50, blank=True)
#
# 	class Meta:
#         managed = False
#         db_table = 'channel'
#
# 	def __str__(self):
# 		return '%s' % (self.channelname)
#
#
#
# class Industry(models.Model):
#     industryid = models.IntegerField(primary_key=True)
#     industryname = models.CharField(max_length=50)
# 	industry_channel_price = models.ManyToManyField(channel, through='channel_industry_price')
#
#     class Meta:
#         managed = False
#         db_table = 'industry'
#
# 	def __str__(self):
# 		return '%s' % (self.industryname)
#
#
#
# class Channel_Industry_Price(models.Model):
#     channel_industry_price_id = models.IntegerField(primary_key=True)
#     channelid = models.ForeignKey(channel, db_column='channelid')
#     industryid = models.ForeignKey(industry, db_column='industryid')
#     price_per_click = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#     price_impression = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'channel_industry_price'
# 		unique_together = ("channelid", "industryid")
#
#
#
# class Product_Dictionary(models.Model):
#     product_id = models.IntegerField(primary_key=True)
#     eng_kw = models.CharField(unique=True, max_length=50)
#     chn_kw = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'product_dictionary'
#
# 	def __str__(self):
# 		return '%s' % (self.eng_kw)
#
#
#
# class Market_Trend(models.Model):
#     market_trend_id = models.IntegerField(primary_key=True)
#     index_date = models.DateField()
#     product = models.ForeignKey('ProductDictionary')
#     purchase_index1688 = models.DecimalField(max_digits=10, decimal_places=0)
#     purchase_indextb = models.DecimalField(db_column='purchase_indexTb', max_digits=10, decimal_places=0) # Field name made lowercase.
#     supply_index = models.DecimalField(max_digits=10, decimal_places=0)
#
#     class Meta:
#         managed = False
#         db_table = 'market_trend'
# 		unique_together = ("index_date","product_id")
#
#
#
# class User_log(models.Model):
#     usersessionid = models.IntegerField(primary_key=True)
#     industryid = models.ForeignKey(Industry, db_column='industryid')
#     sessiondate = models.DateTimeField()
#     campaign_goal = models.IntegerField()
#     initial_budget = models.DecimalField(max_digits=10, decimal_places=0)
#     comanyname = models.CharField(max_length=50, blank=True)
#     companyurl = models.CharField(max_length=150, blank=True)
#     competitor = models.CharField(max_length=50, blank=True)
#     competitorurl = models.CharField(max_length=150, blank=True)
#     productname = models.CharField(max_length=50, blank=True)
#     class Meta:
#         managed = False
#         db_table = 'userlog'
