from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from member_service.models import Product_Dictionary_C1, Product_Dictionary_C2, Product_Dictionary_C3, Market_Trend
import json
import time
import datetime
import random


def getCat1(request):
    all_cats1 = Product_Dictionary_C1.objects.all()
    result = []
    for cat1 in all_cats1:
        result.append({ 'id': str(cat1.cat1_id), 'eng_kw': cat1.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')

def getCat2(request, cat1):
    all_cats2 = Product_Dictionary_C2.objects.filter(cat1_id = cat1)
    result = []
    for cat2 in all_cats2:
        result.append({ 'id': str(cat2.cat2_id), 'eng_kw': cat2.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')

def getCat3(request, cat2):
    all_cats3 = Product_Dictionary_C3.objects.filter(cat2_id = cat2)
    result = []
    for cat3 in all_cats3:
        result.append({ 'id': str(cat3.cat3_id), 'eng_kw': cat3.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')

# def stage2_result(request, cat1, cat2, cat3):
#     result = get_market_trend(cat1, cat2, cat3)
#     context = {'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'trend_result': result}
#     return render(request, 'member_service/ssp.html', context)
#



def index(request):
    #return HttpResponse("Hello, world!")
    #return render_to_string('default_web/index.html',{})
    return render(request, 'default_web/index.html', {})

def product_and_service(request):
    return render(request, 'default_web/pns.html',{})

def about(request):
    return render(request, 'about.html',{})

def member_service(request):
    return render(request, 'member_service.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def testimonials(request):
    return render(request, 'default_web/testimonials.html',{})

def education_case(request):
    return render(request, 'default_web/education_case.html',{})
def destination_mkt_case(request):
    return render(request, 'default_web/destination_mkt_case.html',{})
def real_estate_case(request):
    return render(request, 'default_web/real_estate_case.html',{})
def high_tech_case(request):
    return render(request, 'default_web/high_tech_case.html',{})


def stage1(request):
    context = request.GET.dict()
    if len(context) == 0:
        today = datetime.date.today()
        demo_purchase_index1688, demo_purchase_indexTb, demo_supply_index = [], [], []
        for i in range(365, -1, -1):
            sample_date = today - datetime.timedelta(days=i)
            epoch = int(time.mktime(sample_date.timetuple())) * 1000
            # demo_purchase_index1688.append([ epoch, random.randint(0, 5000) ])
            # demo_purchase_indexTb.append([ epoch, random.randint(0, 5000) ])
            # demo_supply_index.append([ epoch, random.randint(0, 5000) ])
            period = i / 15 % 15
            demo_purchase_index1688.append([ epoch, random.randint(period * 1000, (period + 1) * 1000) ])
            demo_purchase_indexTb.append([ epoch, random.randint(period * 1000, (period + 1) * 1000) ])
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
            epoch = int(time.mktime(record.index_date.timetuple())) * 1000
            purchase_index1688.append([ epoch, int(record.purchase_index1688) ])
            purchase_indexTb.append([ epoch, int(record.purchase_indextb) ])
            supply_index.append([ epoch, int(record.supply_index) ])
        context['purchase_index1688'] = purchase_index1688
        context['purchase_indexTb'] = purchase_indexTb
        context['supply_index'] = supply_index
    return render(request, 'default_web/stage1.html', context)

def budget_allocation_test(request):
    return render(request, 'default_web/stage2_test.html', {})
def stage2_result(request):
    return render(request, 'default_web/stage2_result.html', {})

def wave_test(request):
    return render(request, 'default_web/stage3_test.html', {})
def stage3_result(request):
    return render(request, 'default_web/stage3_result.html', {})






