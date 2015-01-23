'''
Get price, sales and supply trends data from alizs
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

from initialization import crawling_init, translate
import codecs
# import translate

def get_ali_index_test(keyword):
    '''
    Read each keyword in English and do a test crawling from index.1688.com.
    If the index of the keyword can be found, return 1, otherwise return None 
    '''

    # Remove leading and trailing spaces
    keyword = keyword.strip()
    if keyword == '':
        return {}
    else:       
        keyword = translate(keyword)['chinese']
        #keyword = urllib.quote_plus(cnkey.encode('gb2312'))
def get_ali_index(keyword):
    '''
    Pre-condition: all keywords in database can be indexed in index.1688.com.
    Read keyword object from database,which include the word ID, English format and Chinese format.
    Crawl the keyword and return all index data in a dictionary. If no data return for some reason, return None.
    Note: here keyword is an object instead of a string.
    '''
    print 'the searched key in chinese is ', keyword['chinese']

    # query url
    #qurl = "http://index.1688.com/alizs/market.htm?keywords=" + key
    qurl = "http://index.1688.com/alizs/market.htm?keywords=" + keyword['chinese'].encode('utf8')

    print 'searched url for market index = ', qurl
    # pdb.set_trace()
    data = {}
    html = crawling_init(qurl)

    if html:
        soup = BeautifulSoup(html)
        # If Alizs does not have the data for current keyword, return empty data
        moderror  = soup.findAll('p',{'class':'search-tip'})
        # print 'len(moderror) = ', len(moderror)
        if len(moderror) >= 1:
            print moderror
            return {}
        # Otherwise, retrieve data
        else:
        # comment out the getting data code for testing
        # the commented code is still useful
            datadiv = soup.findAll('input')
            rawdata = str(datadiv[5])


            # Retrieve trends data
            dataidx1 = [(a.start(),a.end()) for a in list(re.finditer("history\"\:\[",rawdata))]
            # print 'dataidx1 = ', dataidx1
            dataidx2 = [(a.start(),a.end()) for a in list(re.finditer("\]\}",rawdata))]
            # print 'dataidx2 = ', dataidx2

            purchase_index1688 = rawdata[dataidx1[1][1]:dataidx2[1][0]]
            data['purchase_index1688'] = purchase_index1688.split(",")
            purchase_indexTb = rawdata[dataidx1[3][1]:dataidx2[3][0]]
            data['purchase_indexTb'] = purchase_indexTb.split(",")
            #print len(data['price'])
            supply_index = rawdata[dataidx1[5][1]:dataidx2[5][0]]
            data['supply_index'] = supply_index.split(",")

            # Retrieve last date
            dateidx1 = html.find("lastDate")
            tmp = html[dateidx1:]
            dateidx2 = tmp.find("\"/>")
            temp = html[dateidx1+31:dateidx1+dateidx2]
            d_last = datetime.datetime.strptime(temp,'%Y-%m-%d').date()
            # print 'last date = ', d_last
            daydiff = len(data['purchase_index1688'])
            # print 'daydiff = ', daydiff  #366

            ali_date=[]
            for i in range(daydiff):
                day = d_last-datetime.timedelta(daydiff-1-i)
                # print 'the day is: ', day
                # pdb.set_trace()
                ali_date.append(day)
            data['date'] = ali_date
    else:
        print 'the web page is empty'

    return data

if __name__ == "__main__":

    print 'sys.argv = ', sys.argv
    print 'sys.argv = ', sys.argv[1:]   

    print 'keyword = ', sys.argv[1]
    
    result = get_ali_index(sys.argv[1])
    if result:
        # for i in range(len(result['date'])):
        #     print result['date'][i],'\t',result['purchase_index1688'][i],'\t', result['purchase_indexTb'][i],'\t', result['supply_index'][i]
        print 'get result successfully for ', sys.argv[1]
    else:
        print 'no result for ', sys.argv[1]
    #print 'result = ', results
 
