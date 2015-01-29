from django.shortcuts import render
from django.http import HttpResponse

# models import for test purpose
from getAliIndex import get_ali_index
# Create your views here.
from initialization import db_connection
from read_from_db import get_market_trend
import datetime



#def sales_signal_processing(request):
def sales_signal_processing(request,keyword=None, date_start=None, date_end=None):
	# before database has been set up, use 'valve' sample data
	# comments below after database has been setup

	# data = get_ali_index('valve')
	#data = get_market_trend('stainless steel mineral spring pump','2014-03-06','2014-12-06')
	zipped_data={}
	zipped_data['error'] = "1"
	if request.method == 'GET':
		if ('keyword' in request.GET) and (request.GET['keyword']!= '') :
			keyword = request.GET['keyword'].strip()
			if (('date_start' in request.GET) and (request.GET['date_start'] != '')):
				date_s = request.GET['date_start']
				print date_s
				date_start =datetime.datetime.strptime(date_s,'%m/%d/%Y').date()
			else:
				date_start = datetime.date.today()-datetime.timedelta(364)
			if (('date_end' in request.GET) and (request.GET['date_end'] !='')):
				date_e = request.GET['date_end']
				date_end =datetime.datetime.strptime(date_e,'%m/%d/%Y').date()
			else:
				date_end = datetime.date.today()

			print "keyword:" + keyword
			print "start date: "+ date_start.strftime("%B %d, %Y")
			print "end date: "+ date_end.strftime("%B %d, %Y")
			data = get_market_trend(keyword,date_start,date_end)

			if data=={}:
				zipped_data['error'] = "1"
				print "error: "+zipped_data['error']
			else:
				zipped_data['error']= "0"
				zipped_data['result'] = zip(data['date'],data['purchase_index1688'], data['purchase_indexTb'], data['supply_index'])
				zipped_data['keyword'] = data['keyword']
				zipped_data['key_cn'] = data['key_cn']
				print "error: "+zipped_data['error']
	return render(request, 'member_service/ssp.html',zipped_data)
	# end of comments for pre-database code 

def ssp_search(request):
	return render(request,'member_service/ssp_search.html',{})

def wave(request):
	return render(request,'member_service/wave.html',{})

def endu(request):
	return render(request,'member_service/endu.html',{})

def twins(request):
	return render(request, 'member_service/twins.html',{})

def base_test(request):
	return render(request, 'member_service/base_test.html',{})