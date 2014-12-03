from django.forms import widgets
from rest_framework import serializers
from restapi.models import Task


#Serializer for account
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('AccountID', 'Email', 'FirstName', 'LastName', 'Title', 'L_ID', 'C_ID',
                  'SignUpDate', 'Subscription', 'Status')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.AccountID = attrs.get('AccountID', instance.AccountID)
            instance.Email = attrs.get('Email', instance.Email)
            instance.FirstName = attrs.get('FirstName', instance.FirstName)
            instance.LastName = attrs.get('LastName', instance.LastName)
            instance.Title = attrs.get('Title', instance.Title)
            instance.L_ID = attrs.get('L_ID', instance.L_ID)
            instance.C_ID = attrs.get('C_ID', instance.C_ID)
            instance.SignUpDate = attrs.get('SignUpDate', instance.SignUpDate)
            instance.Subscription = attrs.get('Subscription', instance.Subscription)
            instance.Status = attrs.get('Status', instance.Status)
            return instance

        # Create new instance
        return Account(**attrs)
    
    
#Serializer for Keywords   
class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = ('KeywordID', 'Keyword', 'Status')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.KeywordID = attrs.get('KeywordID', instance.KeywordID)
            instance.Keyword = attrs.get('Keyword', instance.Keyword)
            instance.Status = attrs.get('Status', instance.Status)
            
            return instance

        # Create new instance
        return Keywords(**attrs)
    
#Serializer for News
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('NewsID', 'News', 'NDate', 'URL', 'Summary', 'M_ID', 'Zipcode',
                  'type', 'InsertDate')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.NewsID = attrs.get('NewsID', instance.NewsID)
            instance.News = attrs.get('News', instance.News)
            instance.NDate = attrs.get('NDate', instance.NDate)
            instance.URL = attrs.get('URL', instance.URL)
            instance.Summary = attrs.get('Summary', instance.Summary)
            instance.M_ID = attrs.get('M_ID', instance.M_ID)
            instance.Zipcode = attrs.get('Zipcode', instance.Zipcode)
            instance.type = attrs.get('type', instance.type)
            instance.InsertDate = attrs.get('InsertDate', instance.InsertDate)
            
            return instance

        # Create new instance
        return News(**attrs)
    
#Serializer for Glogou_News view      
class Glogou_NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glogou_News
        fields = ('NewsID', 'Title', 'NDate', 'URL', 'Summary', 'MediaName', 'Keyword',
                  'InsertDate')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.NewsID = attrs.get('NewsID', instance.NewsID)
            instance.Title = attrs.get('Title', instance.Title)
            instance.NDate = attrs.get('NDate', instance.NDate)
            instance.URL = attrs.get('URL', instance.URL)
            instance.Summary = attrs.get('Summary', instance.Summary)
            instance.MediaName = attrs.get('MediaName', instance.MediaName)
            instance.Keyword = attrs.get('Keyword', instance.Keyword)
            instance.InsertDate = attrs.get('InsertDate', instance.InsertDate)
            
            return instance

        # Create new instance
        return Glogou_News(**attrs)
    
#Serializer for Account_Keywords   
class Account_KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Keywords
        fields = ('A', 'K', 'Id')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.A_ID = attrs.get('A', instance.A_ID)
            instance.K_ID = attrs.get('K', instance.K_ID)
            instance.Id = attrs.get('Id', instance.Id)
            
            return instance

        # Create new instance
        return Account_Keywords(**attrs)
    
#Serializer for News_Keywords    
class News_KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Keywords
        fields = ('N_ID', 'K_ID', 'Id')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.N_ID = attrs.get('N_ID', instance.N_ID)
            instance.K_ID = attrs.get('K_ID', instance.K_ID)
            instance.Id = attrs.get('Id', instance.Id)
            
            return instance

        # Create new instance
        return News_Keywords(**attrs)