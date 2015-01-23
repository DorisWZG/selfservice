''' 
database reading task include translate product name from English to Chinese, and get a product market trend from database etc.
'''

# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import re
import warnings
import json
import mechanize
import cookielib
import urllib, urllib2
import sys
import pprint
import datetime
import pdb

from initialization import db_connection, translate


def get_market_trend(keyword,date_start, date_end):
    '''given an product name, begin date and end date, get all supply and demand index from taobao and aliz
    return the data in dictionary form to ease future processing and presenting'''

    db = None
    data= {}
    start_date = date_start
    end_date = date_end
    #pdb.set_trace()
    product = translate(keyword)
    if product:
        print 'product id = ', product['id']
        #pdb.set_trace()
        try:
            db = db_connection()
            cur = db.cursor()
            
            #query = "SELECT * FROM market_trend WHERE (%s >= %s AND %s<= %s) ORDER BY 'date' ASC;" % ('date','date', start_date, end_date)
            query = "SELECT * FROM market_trend WHERE (product_id=%s AND index_date >= \'%s\' AND index_date<= \'%s\') ORDER BY 'index_date' ASC;" % (product['id'],start_date, end_date)
            print 'query: ', query
            cur.execute(query)
            results = cur.fetchall()


            if results:    
                data= { 'purchase_index1688': [], 
                        'purchase_indexTb': [], 
                        'supply_index': [], 
                        'date': [],
                        'keyword':keyword,
                        'key_cn': product['chinese'],
                        }

                for row in results: 
                    """check before run if the row[index]/ db design is in right order with this code"""
                    data['purchase_index1688'].append(row[2])
                    data['purchase_indexTb'].append(row[3])
                    data['supply_index'].append(row[4])
                    data['date'].append(row[0])
        except:
            print 'database accessing error occurred.' 
    if db:
        # db.commit()
        db.close()
    return data

if __name__ == "__main__":

    #print 'sys.argv = ', sys.argv
    #print 'sys.argv = ', sys.argv[1:]   
    #start = int(sys.argv[1])
    #stop = int(sys.argv[2])
    #print start,'----', stop
    #result = processing(start, stop)
    result = get_market_trend('skiameter','2013-06-01','2014-05-21')
    #print result['keyword']," : ", result['key_cn']


