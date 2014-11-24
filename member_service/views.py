from django.shortcuts import render
from django.http import HttpResponse

# models import for test purpose
from getAliIndex import get_ali_index
# Create your views here.



def sales_signal_processing(request):
	# before database has been set up, use 'valve' sample data
	data = get_ali_index('valve')
	zipped_data={}
	if data is None:
		zipped_data['error'] = "1"
	else:
		zipped_data['error']= "0"
		zipped_data['result'] = zip(data['date'],data['purchase_index1688'], data['purchase_indexTb'], data['supply_index'])
	return render(request, 'member_service/ssp.html',zipped_data)
		
def wave(request):
	return render(request,'member_service/wave.html',{})

def endu(request):
	return render(request,'member_service/endu.html',{})

def twins(request):
	return render(request, 'member_service/twins.html',{})

def base_test(request):
	return render(request, 'member_service/base.html',{})