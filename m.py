# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Channel(models.Model):
    channelid = models.IntegerField(primary_key=True)
    channelname = models.CharField(max_length=50)
    min_media_buy = models.IntegerField(blank=True, null=True)
    localname = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'channel'

class ChannelIndustryPrice(models.Model):
    channel_industry_price_id = models.IntegerField(primary_key=True)
    channelid = models.ForeignKey(Channel, db_column='channelid')
    industryid = models.ForeignKey('Industry', db_column='industryid')
    price_per_click = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    price_impression = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'channel_industry_price'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Industry(models.Model):
    industryid = models.IntegerField(primary_key=True)
    industryname = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'industry'

class MarketTrend(models.Model):
    market_trend_id = models.IntegerField(primary_key=True)
    index_date = models.DateField()
    product = models.ForeignKey('ProductDictionary')
    purchase_index1688 = models.DecimalField(max_digits=10, decimal_places=0)
    purchase_indextb = models.DecimalField(db_column='purchase_indexTb', max_digits=10, decimal_places=0) # Field name made lowercase.
    supply_index = models.DecimalField(max_digits=10, decimal_places=0)
    class Meta:
        managed = False
        db_table = 'market_trend'

class ProductDictionary(models.Model):
    product_id = models.IntegerField(primary_key=True)
    eng_kw = models.CharField(unique=True, max_length=50)
    chn_kw = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'product_dictionary'

class Userlog(models.Model):
    usersessionid = models.IntegerField(primary_key=True)
    industryid = models.ForeignKey(Industry, db_column='industryid')
    sessiondate = models.DateTimeField()
    campaign_goal = models.IntegerField()
    initial_budget = models.DecimalField(max_digits=10, decimal_places=0)
    comanyname = models.CharField(max_length=50, blank=True)
    companyurl = models.CharField(max_length=150, blank=True)
    competitor = models.CharField(max_length=50, blank=True)
    competitorurl = models.CharField(max_length=150, blank=True)
    productname = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'userlog'

