from django.shortcuts import render
from django.http import HttpResponse

# models import for test purpose
from getAliIndex import get_ali_index
# Create your views here.
from initialization import db_connection
from read_from_db import get_market_trend
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.db.models import Q
from member_service.models import Product_Dictionary_C1, Product_Dictionary_C2, Product_Dictionary_C3, Market_Trend
import json
import time
import datetime
import random
import re

# a global variable to control if URL will show category ID or category name
# __IMPORTANT_NOTE__, this setting needs to be consistent with sales_opportunities.js
g_URL_SHOW_CAT_ID_OR_NAME = 0       # 0, show category ID, 1, show category name

# function ValidPhone(...) , ValidEmail(...) and subscriber_contact(...) related to subscriber newsletter
def ValidPhone(p):
    if re.search(r'[^\.\(\)\-0-9]', p):
        return False
    else:
        seq_type = type(p)
        p = seq_type().join(filter(seq_type.isdigit, p))
        try:
            int(p)
            if len(p)>4:
                return True
        except:
            return False

def ValidEmail(m):
    if re.match(r"[^@]+@[^@]+\.[^@]+", m):
        return True
    else:
        return False

def subscriber_contact(request):
    errors = []
    context = create_demo_data()
    if request.method == 'POST':
        if not request.POST.get('name'):
            errors.append('Enter your name.')
        if not ValidPhone(request.POST.get('number')):
            errors.append('Enter your contact number.')
        if not request.POST.get('CompanyName'):
            errors.append('Enter your company name.')
        if not ValidEmail(request.POST.get('email')):
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('message'):
            errors.append('Enter industry and product categories.')
        if not errors:
            send_mail(
                'Opportunity Alert Subscriber',
                "Name:"+request.POST['name']+ " " + "Contact number:"+request.POST['number']+ " " + "Company name:"+ request.POST['CompanyName'] + " " + "email:"+ request.POST['email'] + " " + "Message:" + request.POST['message'],
                'glogoutest@gmail.com',
                ['help@glogou.com']
            )
            return render(request, 'member_service/subscriber_contact.html', context)

    context.update({
        'errors': errors,
        'name': request.POST.get('name'),
        'number': request.POST.get('number'),
        'CompanyName': request.POST.get('CompanyName'),
        'email': request.POST.get('email'),
        'message': request.POST.get('message')
    })
    return render(request, 'member_service/subscriber_contact.html', context)

## getCat1(...), getCat2(...), getCat3(...) are used in Javascript
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

    # demo mode, we will generate some demo data.
    if len(context) == 0:
        context = create_demo_data()

    elif 'cat1' in context and len(context['cat1'].strip()) > 0:

        if(g_URL_SHOW_CAT_ID_OR_NAME == 0):
            criteria, context = create_query_use_cat_ID(context)
        else:
            criteria, context = create_query_use_cat_name(context)

        # query database to get market trend data.
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

# create demo data.
def create_demo_data():

        context = {}

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
        context['cat1'] = None
        context['cat2'] = None
        context['cat3'] = None

        return context

# create a query similar like: 'cat1=1&cat2=128&cat3=142'
def create_query_use_cat_ID(context):

        criteria = Q(cat1_id=context['cat1'])

        if 'cat2' in context and len(context['cat2'].strip()) > 0:
            criteria &= Q(cat2_id=context['cat2'])

            if 'cat3' in context and len(context['cat3'].strip()) > 0:
                criteria &= Q(cat3_id=context['cat3'])

        return criteria, context

# create a query similar like: 'cat1=Agriculture&cat2=Agricultural+equipment&cat3=Fishing+equipment'
# Note, in this function, , we also update content of 'cat1', 'cat2', 'cat3' to category id,
# because the input of this function, context, the content of 'cat1', 'cat2', 'cat3' original only
# contain category names. We update it to category id because at this moment, the template file
# sales_opportunities.html expect the content of 'cat1', 'cat2', 'cat3' are category id. __NOTE_BL__
# In future, if we update template file sales_opportunities.html to ake category name, then we do not
# do this update.
def create_query_use_cat_name(context):

        # Have to set to None in case category is not set.
        criteria_cat1_id = None
        criteria_cat2_id = None
        criteria_cat3_id = None

        #if "pass in" is category name, instead of cat_id
        tmp =context['cat1']
        criteria_cat1 = Product_Dictionary_C1.objects.filter(eng_kw = tmp)

        if(len(criteria_cat1) == 1):
            criteria_cat1_id = criteria_cat1[0].cat1_id
            criteria_cat = Q(cat1_id=criteria_cat1_id)

        if 'cat2' in context and len(context['cat2'].strip()) > 0:

            #if "pass in" is category name, instead of cat_id
            tmp = context['cat2']
            criteria_cat2= Product_Dictionary_C2.objects.filter(eng_kw = tmp)

            # if a category is NOT selected, the following condition will not meet.
            if(len(criteria_cat2) == 1):
                criteria_cat2_id = criteria_cat2[0].cat2_id
                criteria_cat &= Q(cat2_id=criteria_cat2_id)

            if 'cat3' in context and len(context['cat3'].strip()) > 0:

                #if "pass in" is category name, instead of cat_id
                tmp =  context['cat3']
                criteria_cat3 = Product_Dictionary_C3.objects.filter(eng_kw = tmp)

                # if a category is NOT selected, the following condition will not meet.
                if(len(criteria_cat3) == 1):
                    criteria_cat3_id = criteria_cat3[0].cat3_id
                    criteria_cat &= Q(cat3_id=criteria_cat3_id)

        #  We update the content of 'cat1', 'cat2', 'cat3' to category id
        #  because at this moment, the template file sales_opportunities.html expect this format. __BL_NOTE__
        context.update({
            'cat1': criteria_cat1_id,
            'cat2': criteria_cat2_id,
            'cat3': criteria_cat3_id
        })

        return criteria_cat, context

# This is an old version, no longer in need anymore
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