__author__ = 'Yuer'
import json
from pprint import pprint
import datetime
from member_service.models import Market_Trend, Product_Dictionary_C1, Product_Dictionary_C2
from initialization import db_connection

def read_json_obj(filename):
    # db = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "self_service")
    # cur = db.cursor()
    with open(filename) as data_file:
        data = json.load(data_file)
    # pprint(data)

    for item in data:
        cats = item['cat'].split(',')
        cats_len = len(cats)
        cat1 = cats[0] if cats_len > 0 else 0
        cat2 = cats[1] if cats_len > 1 else 0
        cat3 = cats[2] if cats_len > 2 else 0
        index_len = len(item['purchase_index1688'])
        d_last = datetime.datetime.strptime(item['d_last'],'%Y-%m-%d').date()
        latest_date = check_latest_record(cat1, cat2, cat3)
        for i in range(0, index_len):
            cur_date = d_last-datetime.timedelta(item['daydiff']-1-i)
            if latest_date is None or latest_date < cur_date:
                record =  Market_Trend()
                record.index_date = cur_date
                record.cat1_id, record.cat2_id, record.cat3_id = cat1, cat2, cat3
                record.supply_index = item['supply_index'][i]
                record.purchase_index1688 = item['purchase_index1688'][i]
                record.purchase_indextb = item['purchase_indexTb'][i]
                record.save()

def check_latest_record(cat1, cat2, cat3):
    db = None
    latest_date = None
    try:
        db = db_connection()
        cur = db.cursor()
        query = "SELECT * FROM market_trend WHERE cat1_id = %s and cat2_id = %s and cat3_id = %s ORDER BY index_date DESC LIMIT 1" %(cat1,cat2,cat3)
        # print query
        cur.execute(query)
        latest_date = cur.fetchone()[1]
    except:
        print "database accessing error!"

    db.close()
    return latest_date

def read_cat1(fileCat1):


    with open(fileCat1) as data:
        for item in data:
            print item
            cat1 = item.split("---")

            record = Product_Dictionary_C1()

            record.cat1_id = cat1[1]
            record.chn_kw = cat1[0]
            record.eng_kw = cat1[2]
            record.save()

def read_cat2(fileCat2):


    with open(fileCat2) as data:
        for item in data:
            print item
            cat1 = item.split("---")

            record = Product_Dictionary_C2()

            # Product_Dictionary_C1.objects.create(record.cat1_id = Product_Dictionary_C1.cat1_id)
            record.cat2_id = cat1[2]
            record.chn_kw = cat1[0]
            record.eng_kw = cat1[2]
            record.save()

fileCat1 = '../product_name_en_ch_list_cat1.txt'
read_cat1(fileCat1)

filename = '../crawled_results_1_3.txt'
read_json_obj(filename)
