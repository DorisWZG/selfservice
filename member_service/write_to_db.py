__author__ = 'Yuer'

# This script will load data to database 
# To run this script, one need to 
# 1. set up path for django settings.
# 2. set up path for crawled data files (need to have those crawled data file first, five of them. on github crawler depository. 
#    after get from github, need to uncompress them and put into some directories.
# 3. set up path for categories files (need to have those categories files, three of them).
#
# Note: for some reasons we do not understand yet, this script is very slow, 
#       to speed up, we temporarily disable check data record in read_json_obj        #latest_date = check_latest_record(cat1, cat2, cat3)

import os
import sys
import json
#sys.path.append("/home/dev/Workspace/sspEnvFolder/self_service_platform/SelfService/")
sys.path.append("C:\\tmp3\\projects\\SelfService\\")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selfservice.settings')

import django
from pprint import pprint
import datetime
from member_service.models import Market_Trend,Product_Dictionary_C1,Product_Dictionary_C2,Product_Dictionary_C3
from initialization import db_connection
import codecs
# import django
# django.setup()
# import mysql
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

            #latest_date = check_latest_record(cat1, cat2, cat3)
            # _BL_, tempoary not check date record
            latest_date = None

            for i in range(0, index_len):
                cur_date = d_last-datetime.timedelta(item['daydiff']-1-i)
                if latest_date is None or latest_date < cur_date:
                    record =  Market_Trend()
                    record.index_date = cur_date
                    record.cat1_id, record.cat2_id, record.cat3_id = cat1, cat2, cat3
                    record.supply_index = item['supply_index'][i]
                    record.purchase_index1688 = item['purchase_index1688'][i]
                    record.purchase_indextb = item['purchase_indexTb'][i]
                    #print record.supply_index
                    try:
                        record.save()
                    except:
                        break



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


def load_to_db_recursive_one_dir(dir_name, fail_log_name, all_log_name, all_file_name):

    cnt = 0
    error_cnt = 0

    for root, dirs, files in os.walk(dir_name):
        for name in files:
           filename = os.path.join(root,name)
           #print filename
           if "crawled_results" in filename:
               cnt += 1
               print 'cnt %d'%(cnt)
               print filename
               try:
                   all_file_name.write(filename)
                   all_file_name.flush()
               except:
                   error_cnt += 1
                   print '=============Failed: write: filename %s, error_cnt %d'%(filename, error_cnt)
                   continue

               try:
                    read_json_obj(filename,fail_log_name,all_log_name)
               except:
                   error_cnt += 1
                   print '=============Failed: read_json, filename %s, error_cnt %d'%(filename, error_cnt)
                   continue

        print 'All complete ! dir_name %s, cnt %d, error_cnt %d'%(dir_name, cnt, error_cnt)
        
        return cnt, error_cnt

# Load category file to database
read_cat1()
read_cat2()
read_cat3()

#filename = '../crawled_results_1_10.txt'
#read_json_obj(filename)
fail_log_name = open("fail_log.txt","w")
all_log_name = open("all_log.txt","w")
all_file_name = open("all_file.txt",'w')

# NEED to set up the path for the crawled data
# There are total five sets of crawled results file
dir_results_initial_crawl = '../crawled_market_trend_results/results_initial_crawl'
dir_results_all_fail_recrawl = '../crawled_market_trend_results/results_all_fail_recrawl'
dir_results_all_fail_fail_recrawl = '../crawled_market_trend_results/results_all_fail_fail_recrawl'
dir_results_cat1_has_cat2 = '../crawled_market_trend_results/cat1_has_cat2_crawled_results54' 
dir_results_cat2_has_cat3 = '../crawled_market_trend_results/cat2_has_cat3_crawled_results723' 

cnt_initial_crawl, err_cnt_initial_crawl          = load_to_db_recursive_one_dir(dir_results_initial_crawl, fail_log_name, all_log_name, all_file_name)
cnt_fail_recrawl, err_cnt_fail_recrawl            = load_to_db_recursive_one_dir(dir_results_all_fail_recrawl, fail_log_name, all_log_name, all_file_name)
cnt_fail_fail_recrawl, err_cnt_fail_fail_recrawl  = load_to_db_recursive_one_dir(dir_results_all_fail_fail_recrawl, fail_log_name, all_log_name, all_file_name)
cnt_cat1_has_cat2, err_cnt_cat1_has_cat2          = load_to_db_recursive_one_dir(dir_results_cat1_has_cat2, fail_log_name, all_log_name, all_file_name)
cnt_cat2_has_cat3, err_cnt_cat2_has_cat3          = load_to_db_recursive_one_dir(dir_results_cat2_has_cat3, fail_log_name, all_log_name, all_file_name)

all_file_name.write('\n\n')

tmp = 'cnt_initial_crawl %d, err_cnt_initial_crawl %d\n'%(cnt_initial_crawl, err_cnt_initial_crawl)
all_file_name.write(tmp)

tmp = 'cnt_fail_recrawl %d, err_cnt_fail_recrawl %d\n' %(cnt_fail_recrawl, err_cnt_fail_recrawl)
all_file_name.write(tmp)

tmp = 'cnt_fail_fail_recrawl %d, err_cnt_fail_fail_recrawl %d\n' %(cnt_fail_fail_recrawl, err_cnt_fail_fail_recrawl)
all_file_name.write(tmp)

tmp = 'cnt_cat1_has_cat2 %d, err_cnt_cat1_has_cat2 %d\n' %(cnt_cat1_has_cat2, err_cnt_cat1_has_cat2)       
all_file_name.write(tmp)
   
tmp = 'cnt_cat2_has_cat3 %d, err_cnt_cat2_has_cat3 %d\n' %(cnt_cat2_has_cat3, err_cnt_cat2_has_cat3)
all_file_name.write(tmp)


all_file_name.close()
all_log_name.close()
fail_log_name.close()
