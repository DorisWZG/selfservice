__author__ = 'Yuer'
import os
import sys
import json
from pprint import pprint
import datetime
from member_service.models import Market_Trend,Product_Dictionary_C1,Product_Dictionary_C2,Product_Dictionary_C3
from initialization import db_connection
import codecs
import django
django.setup()
import mysql
from django.db import IntegrityError, DataError

def read_json_obj(filename,fail_log_name, all_log_name):
    # db = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "self_service")
    # cur = db.cursor()
    with open(filename) as data_file:
        data = json.load(data_file)
    # pprint(data)
    s1 = ''
    try:
        for item in data:
            cats = item['cat'].split(',')
            cats_len = len(cats)
            cat1 = cats[0] if cats_len > 0 else 0
            cat2 = cats[1] if cats_len > 1 else 0
            cat3 = cats[2] if cats_len > 2 else 0
            s1 = str(cat1) + " " + str(cat2) + " " + str(cat3) + "\n"
            print s1
            all_log_name.write(s1)
            all_log_name.flush()
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
                    print record.supply_index
                    record.save()



    except:
        s1 = str(cat1) + " " + str(cat2) + " " + str(cat3) + "write json error\n"
        print s1
        fail_log_name.write(s1)
        fail_log_name.flush()

        all_log_name.write(s1)
        all_log_name.flush()



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

def read_cat1():
    with open('../product_name_en_ch_list_cat1.txt') as data:
        for item in data:
            #print item
            cat1 = item.split("---")

            record = Product_Dictionary_C1()
            record.cat1_id = cat1[1]
            record.chn_kw = cat1[0]
            record.eng_kw = cat1[2]
            record.save()

def read_cat2():
    cnt = 0
    with codecs.open("../cat_level2.txt",'r','utf-8') as cat2File:
        with open("../product_name_en_list_cat2.txt") as engFile:
            for item in cat2File:
                cnt += 1
                print cnt
                new_item = item.replace(" --- ",' | ').replace("\r","").replace("\n", "").strip()
                cat2 = new_item.split(' | ')
                # cat2[0] cat1 Ch, cat2[1] cat2 ch, cat2[2] cat1 id, cat2[3] cat2 id
                #print cat2
                record = Product_Dictionary_C2()
                record.cat2_id = cat2[3]
                record.chn_kw = cat2[1]
                record.eng_kw = engFile.readline()

                # record.pd_c1_id = cat2[2]

                rec = Product_Dictionary_C1()
                rec.cat1_id = cat2[2]
             #   rec = Product_Dictionary_C1.objects.get(cat1_id = cat2[2])

                #record.pd_c1_id. = rec.cat1_id
                record.cat1 = rec


                record.save()


def read_cat3():
    cnt = 0
    cnt2 = 0

    with codecs.open("../cat_level3.txt",'r','utf-8') as cat3File:
        with open("../product_name_en_list_cat3.txt") as engFile:
            #ef = codecs.open('errfile.txt','w','utf-8')
            #cf = codecs.open('file.txt','w','utf-8')
            str = ""
            for item in cat3File:
                cnt += 1
                print "chFile:",cnt
                new_item = item.replace(" --- ",' | ').replace("\r","").replace("\n", "").strip()
                cat3 = new_item.split(' | ')
                if("#" in cat3):
                    continue
                # cat2[0] cat1 Ch, cat2[1] cat2 ch, cat2[2] cat1 id, cat2[3] cat2 id
                #print cat2
                cnt2 += 1
                print "engFile:",cnt2
                record = Product_Dictionary_C3()
                record.cat3_id = cat3[5]

                record.chn_kw = cat3[2]
                record.eng_kw = engFile.readline()
                print record.cat3_id, record.chn_kw, record.eng_kw
                #record.pd_c1_id = cat2[2]

                rec = Product_Dictionary_C2()
                rec.cat2_id = cat3[4]

                record.cat2 = rec
                str = record.chn_kw + record.eng_kw

                #cf.write(str)

                record.save()
                '''
                try:
                    record.save()
                except IntegrityError:
                    print record.cat3_id, record.chn_kw, record.eng_kw

                    str = record.chn_kw +" "+ record.eng_kw
                    ef.write(str)
                except DataError:
                    print("dataerr")
                    print("err")
                    str = record.chn_kw + record.eng_kw +"err2"
                    ef.write(str)
                '''
            #cf.close()
            #ef.close()


read_cat1()
read_cat2()
read_cat3()

#filename = '../crawled_results_1_10.txt'
#read_json_obj(filename)
fail_log_name = open("fail_log.txt","w")
all_log_name = open("all_log.txt","w")
all_file_name = open("all_file.txt",'w')
cnt = 0
for root, dirs, files in os.walk('../result'):
    for name in files:
       filename = os.path.join(root,name)
       #print filename
       if "crawled_results" in filename:
           cnt += 1
           print cnt
           print filename
           all_file_name.write(filename)
           all_file_name.flush()
           read_json_obj(filename,fail_log_name,all_log_name)
all_file_name.close()
all_log_name.close()
fail_log_name.close()
