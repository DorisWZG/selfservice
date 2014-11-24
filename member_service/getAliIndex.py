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
from initialization import crawling_init
# import translate

def get_ali_index(keyword):

    # Remove leading and trailing spaces
    keyword = keyword.strip()   
    if keyword == '':
        return {}
    else:       
        # keyword = translate(keyword)['chinese']
        # keyword = urllib.quote_plus(cnkey.encode('gb2312'))
        print 'searched key is ', keyword
            
        # query url   
        #qurl = "http://index.1688.com/alizs/market.htm?keywords=" + key
        qurl = "http://index.1688.com/alizs/market.htm?keywords=" + keyword
        # print 'qurl = ', qurl
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
            print 'the webpage is empty'
        
        return data

if __name__ == "__main__":

    print 'sys.argv = ', sys.argv
    print 'sys.argv = ', sys.argv[1:]   

    print 'keyword = ', sys.argv[1]
    
    result = get_ali_index(sys.argv[1])
    if result:
        for i in range(len(result['date'])):
            print result['date'][i],'\t',result['purchase_index1688'][i],'\t', result['purchase_indexTb'][i],'\t', result['supply_index'][i]
    #print 'result = ', results
 