from django.shortcuts import render
from django.http import HttpResponse

# models import for test purpose
from getAliIndex import get_ali_index
# Create your views here.
from initialization import db_connection
from read_from_db import get_market_trend
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.db.models import Q
from member_service.models import Product_Dictionary_C1, Product_Dictionary_C2, Product_Dictionary_C3, Market_Trend
import json
import time
import datetime
import random

def subscriber_contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name'):
            errors.append('Enter your name.')
        if not request.POST.get('number'):
            errors.append('Enter your contact number.')
        if not request.POST.get('CompanyName'):
            errors.append('Enter your company name.')
        if not (request.POST.get('email') and '@' in request.POST['email']):
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                'Opportunity Alert Subscriber',
                "Name:"+request.POST['name']+ " " + "Contact number:"+request.POST['number']+ " " + "Company name:"+ request.POST['CompanyName'] + " " + "email:"+ request.POST['email'] + " " + "Message:" + request.POST['message'],
                'glogoutest@gmail.com',
                ['liusicen627@gmail.com']
            )
            return HttpResponseRedirect('*/thanks/')
    #return HttpResponse('Thanks')
    return render(request, 'member_service/subscriber_contact.html', {
        'errors': errors,
        'name': request.POST.get('name'),
        'number': request.POST.get('number'),
        'CompanyName': request.POST.get('CompanyName'),
        'email': request.POST.get('email'),
        'message': request.POST.get('message')
    })

def getCat1(request):
    all_cats1 = Product_Dictionary_C1.objects.all().order_by('eng_kw')
    result = []
    for cat1 in all_cats1:
        result.append({ 'id': str(cat1.cat1_id), 'eng_kw': cat1.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')

def getCat2(request, cat1):
    all_cats2 = Product_Dictionary_C2.objects.filter(cat1_id = cat1).order_by('eng_kw')
    result = []
    for cat2 in all_cats2:
        result.append({ 'id': str(cat2.cat2_id), 'eng_kw': cat2.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')

def getCat3(request, cat2):
    all_cats3 = Product_Dictionary_C3.objects.filter(cat2_id = cat2).order_by('eng_kw')
    result = []
    for cat3 in all_cats3:
        result.append({ 'id': str(cat3.cat3_id), 'eng_kw': cat3.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')

def sales_opportunities(request):
    context = request.GET.dict()
    if len(context) == 0:
        today = datetime.date.today()
        demo_purchase_index1688, demo_purchase_indexTb, demo_supply_index = [], [], []
        for i in range(365, -1, -1):
            sample_date = today - datetime.timedelta(days=i)
            epoch = float(time.mktime(sample_date.timetuple())) * 1000
            # demo_purchase_index1688.append([ epoch, random.randint(0, 5000) ])
            # demo_purchase_indexTb.append([ epoch, random.randint(0, 5000) ])
            # demo_supply_index.append([ epoch, random.randint(0, 5000) ])

            # BL_NOTE, The following random model has no special reasons. We just try different numbers to make
            # the curve looks better. One can feel free to choose different numbers to get better curve
            # The random model has one linear increase component, which is base_increase,
            # together with periodic random model. The period was chosen to be 30 to match days in a month

            step = 30
            period = i / step % step
            period = step - period
            base_increase = (365 -i)*80

            demo_purchase_index1688.append([ epoch, random.randint(1*base_increase + period * 1000, 1*base_increase + 2*(period + 1) * 1000) ])
            demo_purchase_indexTb.append([ epoch, random.randint(2*base_increase + period * 1000, 2*base_increase + 4*(period + 1) * 1000) ])
            demo_supply_index.append([ epoch, random.randint(period * 1000, (period + 1) * 1000) ])

        context['demo_purchase_index1688'] = demo_purchase_index1688
        context['demo_purchase_indexTb'] = demo_purchase_indexTb
        context['demo_supply_index'] = demo_supply_index
    elif 'cat1' in context and len(context['cat1'].strip()) > 0:
        criteria = Q(cat1_id=context['cat1'])
        if 'cat2' in context and len(context['cat2'].strip()) > 0:
            criteria &= Q(cat2_id=context['cat2'])
            if 'cat3' in context and len(context['cat3'].strip()) > 0:
                criteria &= Q(cat3_id=context['cat3'])
        result = Market_Trend.objects.filter(criteria).order_by('index_date')
        purchase_index1688, purchase_indexTb, supply_index = [], [], []
        for record in result:
            epoch = float(time.mktime(record.index_date.timetuple())) * 1000
            purchase_index1688.append([ epoch, int(record.purchase_index1688) ])
            purchase_indexTb.append([ epoch, int(record.purchase_indextb) ])
            supply_index.append([ epoch, int(record.supply_index) ])
        context['purchase_index1688'] = purchase_index1688
        context['purchase_indexTb'] = purchase_indexTb
        context['supply_index'] = supply_index
    return render(request, 'member_service/sales_opportunities.html', context)


#def sales_signal_processing(request):
def sales_signal_processing(request,keyword=None, date_start=None, date_end=None):
    # before database has been set up, use 'valve' sample data
    # comments below after database has been setup

    # data = get_ali_index('valve')
    data = get_market_trend('stainless steel mineral spring pump','2014-03-06','2014-12-06')
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