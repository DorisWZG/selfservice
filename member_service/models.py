from django.db import models

# Create your models here.

class Product_Dictionary(models.Model):
    product_id = models.IntegerField(primary_key=True)
    eng_kw = models.CharField(unique=True, max_length=50)
    chn_kw = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_dictionary'

    def __str__(self):
        return '%s' % (self.eng_kw)



class Market_Trend(models.Model):
    market_trend_id = models.IntegerField(primary_key=True)
    index_date = models.DateField()
    product_id = models.ForeignKey('Product_Dictionary')
    purchase_index1688 = models.DecimalField(max_digits=10, decimal_places=0)
    purchase_indextb = models.DecimalField(db_column='purchase_indexTb', max_digits=10, decimal_places=0) # Field name made lowercase.
    supply_index = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'market_trend'
        unique_together = ("index_date","product_id")

