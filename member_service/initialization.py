''' 
initializing task including
crawling initializing, set up database connector etc.
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

def crawling_init(qurl):
    """query qurl and return corresponding html code, 
    if cannot open browser or not found, return none """   
    print 'qurl = ', qurl

    #Browser
    br = mechanize.Browser()
    
    #Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    
    #Browser options
    br.set_handle_equiv(True)
    #br.set_handel_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    
    #Debugging messages
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    
    #User-Agent
    br.addheaders = [('User-agent','Mozilla/5.0')]
    # br.addheaders = [('user-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    try:
        # open url
        response = br.open(qurl)
        
        # get page content
        html = response.read()
        return html
        
    except: # otherwise, return empty data
        return {}

def db_connection():
    """config mysqldb connection"""

    db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
        user="usr", # your username
        passwd="pwd", # your password
        db="selfservice",
        use_unicode=True,
        charset="utf8") # name of the data base
    return db




