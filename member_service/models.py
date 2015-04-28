from django.db import models

# Create your models here.

class Product_Dictionary_C1(models.Model):
    # pd_c1_id = models.IntegerField(primary_key=True)
    cat1_id = models.DecimalField(primary_key=True, max_digits=15,decimal_places=0)
    eng_kw = models.CharField(unique=True, max_length=50)
    chn_kw = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'product_dictionary_c1'

    def __str__(self):
        return '%s' % (self.eng_kw)

class Product_Dictionary_C2(models.Model):
    # pd_c2_id = models.IntegerField(primary_key=True)
    cat2_id = models.DecimalField(primary_key=True, max_digits=15,decimal_places=0)
    eng_kw = models.CharField(unique=True, max_length=50)
    chn_kw = models.CharField(max_length=50)
    cat1 = models.ForeignKey('Product_Dictionary_C1')

    class Meta:
        # managed = False
        db_table = 'product_dictionary_c2'

    def __str__(self):
        return '%s' % (self.eng_kw)

class Product_Dictionary_C3(models.Model):
    # pd_c3_id = models.IntegerField(primary_key=True)
    cat3_id = models.DecimalField(primary_key=True, max_digits=15,decimal_places=0)
    eng_kw = models.CharField(unique=True, max_length=50)
    chn_kw = models.CharField(max_length=50)
    cat2 = models.ForeignKey('Product_Dictionary_C2')

    class Meta:
        # managed = False
        db_table = 'product_dictionary_c3'

    def __str__(self):
        return '%s' % (self.eng_kw)

class Market_Trend(models.Model):
    # market_trend_id = models.IntegerField(primary_key=True)
    index_date = models.DateField()
    purchase_index1688 = models.DecimalField(max_digits=10, decimal_places=0)
    purchase_indextb = models.DecimalField(db_column='purchase_indexTb', max_digits=10, decimal_places=0) # Field name made lowercase.
    supply_index = models.DecimalField(max_digits=10, decimal_places=0)
    cat1_id = models.DecimalField(max_digits=15,decimal_places=0)
    cat2_id = models.DecimalField(max_digits=15,decimal_places=0,null=True)
    cat3_id = models.DecimalField(max_digits=15,decimal_places=0,null=True)

    class Meta:
        # managed = False
        db_table = 'market_trend'
        unique_together = ("index_date","cat1_id","cat2_id","cat3_id")

